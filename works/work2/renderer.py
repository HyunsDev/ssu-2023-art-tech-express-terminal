import tensorflow as tf
import cv2
import numpy as np
import random
import threading
import time
import p5
from p5react import *
from ..common import Renderer

import builtins

width = 1280
height = 720


class ImageGetter(threading.Thread):
    def __init__(self, condition, camera):
        super(ImageGetter, self).__init__()
        self.image = None
        self.condition = condition
        self.camera = camera

    def get_image(self):
        return self.image

    def run(self):
        while True:
            ret, frame = self.camera.read()
            frame = cv2.resize(frame, (224, 224))
            frame = np.asarray(frame)
            frame = (frame.astype(np.float32) / 127.0) - 1
            frame = np.expand_dims(frame, axis=0)
            with self.condition:
                self.image = frame
                self.condition.notify()  # Notify the inferencer that a new image is ready
            time.sleep(0.01)  # To reduce CPU usage


class ModelInferencer(threading.Thread):
    def __init__(self, condition, interpreter, input_details, output_details):
        super(ModelInferencer, self).__init__()
        self.prediction = None
        self.image = None
        self.new_prediction = False
        self.condition = condition

        self.interpreter = interpreter
        self.input_details = input_details
        self.output_details = output_details

    def set_image(self, image):
        self.image = image

    def get_prediction(self):
        self.new_prediction = False
        return self.prediction

    def run(self):
        while True:
            with self.condition:
                self.condition.wait()  # Wait for a new image to be ready
                if self.image is not None:
                    self.interpreter.set_tensor(
                        self.input_details[0]["index"], self.image
                    )
                    self.interpreter.invoke()
                    self.prediction = self.interpreter.get_tensor(
                        self.output_details[0]["index"]
                    )
                    self.new_prediction = True
                    self.image = None
                time.sleep(0.01)  # To reduce CPU usage


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.targetX = self.x
        self.targetY = self.y
        self.easing = 0.033  # 애니메이션 부드러움 조절
        self.size = random.uniform(10, 50)
        # 동그라미 랜덤 크기 설정

    def move(self):
        dx = self.targetX - self.x
        dy = self.targetY - self.y
        self.x += dx * self.easing
        self.y += dy * self.easing

    def draw(self):
        return (self.x, self.y, self.size, self.size)


# interpreter, input_details, output_details


class Work2Renderer(Renderer):
    def setup(self):
        # TensorFlow Lite 모델 load
        self.interpreter = tf.lite.Interpreter(
            model_path="works/work2/quant_model.tflite"
        )
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # 웹캠 load
        self.camera = cv2.VideoCapture(builtins.cameraId)
        self.camera.set(3, 160)  # width
        self.camera.set(4, 120)  # height

        self.condition = threading.Condition()

        # Pass it to each thread
        self.image_getter = ImageGetter(self.condition, self.camera)
        self.image_getter.start()

        self.model_inferencer = ModelInferencer(
            self.condition, self.interpreter, self.input_details, self.output_details
        )
        self.model_inferencer.start()

        self.circles = []
        self.circleCount = 40  # 동그라미 개수 설정
        self.status = 1

        for _ in range(self.circleCount):
            x = random.uniform(0, 1280)
            y = random.uniform(0, 720)
            circle = Circle(x, y)
            self.circles.append(circle)

        self.graphic = p5.create_graphics(1280, 720)

    def draw(self):
        self.graphic.fill(0, 10)
        self.graphic.rect(0, 0, width, height)
        self.graphic.no_stroke()

        for circle in self.circles:
            circle.move()

            self.graphic.fill(255)
            self.graphic.ellipse(*circle.draw())

        image = self.image_getter.get_image()
        if image is not None:
            self.model_inferencer.set_image(image)

        if self.model_inferencer.new_prediction:
            prediction = self.model_inferencer.get_prediction()

            max_prediction_index = np.argmax(
                prediction
            )  # Save the result of np.argmax()

            # 주먹 - 모임
            if max_prediction_index == 0:
                if self.status == 1:
                    self.status = 0
                    targetX = width / 2
                    targetY = height / 2
                    for circle in self.circles:
                        circle.targetX = targetX
                        circle.targetY = targetY

            # 보자기 - 퍼짐
            elif max_prediction_index == 1:
                if self.status == 0:
                    self.status = 1
                    for circle in self.circles:
                        circle.targetX = random.uniform(0, width)
                        circle.targetY = random.uniform(0, height)

        # self.graphic.fill(0, 10)
        # self.graphic.rect(0, 0, width, height)

        return self.graphic
