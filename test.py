from p5 import *
import glfw


def preload():
    from p5.core.p5 import sketch as p5sketch

    def resize():
        glfw.set_window_size(p5sketch.window, *p5sketch.size)
        p5sketch.resized = True

    p5sketch.resize = resize


def setup():
    size(500, 500)


def draw():
    background(0)
    fill(255)

    graphic = create_graphics(500, 500)
    graphic.circle(mouse_x, mouse_y, 50)

    image(graphic, 0, 0)


run(frame_rate=60, renderer="skia")
