from p5 import *
from works.work1.main import Work1
from element.window import Window

from context import assetsContext, p5Context
from components import TitleComponent, Background, WorkComponent, LoadingScreen
from event import (
    MouseClickedEvent,
    MouseMovedEvent,
    MousePressedEvent,
    MouseReleasedEvent,
    MouseDraggedEvent,
    MouseWheelEvent,
    keyboardEvent,
    KeyPressedEvent,
)

window = Window()


def setup():
    size(p5Context.width, p5Context.height)
    assetsContext.init()

    window.elements.append(Background())
    window.elements.append(LoadingScreen())


def draw():
    window.draw()

    fill(0)
    text_align("LEFT")
    text(str(frame_rate), 10, 10)


def mouse_clicked(event):
    window.dispatchEvent(MouseClickedEvent(event, window))


def mouse_moved(event):
    window.dispatchEvent(MouseMovedEvent(event, window))


def mouse_pressed(event):
    window.dispatchEvent(MousePressedEvent(event, window))


def mouse_released(event):
    window.dispatchEvent(MouseReleasedEvent(event, window))


def mouse_dragged(event):
    window.dispatchEvent(MouseDraggedEvent(event, window))


def mouse_wheel(event):
    window.dispatchEvent(MouseWheelEvent(event, window))


def key_pressed(event):
    window.dispatchEvent(KeyPressedEvent(event))


if __name__ == "__main__":
    run(frame_rate=60)
