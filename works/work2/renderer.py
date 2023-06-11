from ..common.Work import Work

import tensorflow as tf
import cv2
import numpy as np
import random
import threading
import time


class ImageGetter(threading.Thread):
    def __init__(self, condition):
        super(ImageGetter, self).__init__()
        self.image = None
        self.condition = condition

    def get_image(self):
        return self.image

    def run(self):
        global camera
        while True:
            ret, frame = camera.read()
            frame = cv2.resize(frame, (224, 224))
            frame = np.asarray(frame)
            frame = (frame.astype(np.float32) / 127.0) - 1
            frame = np.expand_dims(frame, axis=0)
            with self.condition:
                self.image = frame
                self.condition.notify()  # Notify the inferencer that a new image is ready
            time.sleep(0.01)  # To reduce CPU usage


class ModelInferencer(threading.Thread):
    def __init__(self, condition):
        super(ModelInferencer, self).__init__()
        self.prediction = None
        self.image = None
        self.new_prediction = False
        self.condition = condition

    def set_image(self, image):
        self.image = image

    def get_prediction(self):
        self.new_prediction = False
        return self.prediction

    def run(self, interpreter, input_details, output_details):
        while True:
            with self.condition:
                self.condition.wait()  # Wait for a new image to be ready
                if self.image is not None:
                    interpreter.set_tensor(input_details[0]["index"], self.image)
                    interpreter.invoke()
                    self.prediction = interpreter.get_tensor(output_details[0]["index"])
                    self.new_prediction = True
                    self.image = None
                time.sleep(0.01)  # To reduce CPU usage


# interpreter, input_details, output_details


class Work2Renderer:
    def __init__(self):
        super().__init__("work2", "img2.png", "#000000")

    def setup(self):
        # TensorFlow Lite 모델 load
        self.interpreter = tf.lite.Interpreter(
            model_path="works/work2/quant_model.tflite"
        )
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # 웹캠 load
        self.camera = cv2.VideoCapture(1)
        self.camera.set(3, 160)  # width
        self.camera.set(4, 120)  # height

        self.condition = threading.Condition()

        # Pass it to each thread
        self.image_getter = ImageGetter(self.condition)
        self.image_getter.start()

        self.model_inferencer = ModelInferencer(self.condition)
        self.model_inferencer.start()
