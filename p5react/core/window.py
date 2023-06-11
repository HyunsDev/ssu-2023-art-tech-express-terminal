from .atom import Atom
from .timer import GlobalTimer
from ..events import *
from .assetManager import AssetManager
from .p5react import render
import p5
import glfw
import __main__
from OpenGL import GL
import builtins

__all__ = ["Window"]


class Window(Atom):
    def __init__(self, width, height, title="p5react"):
        self.setWindow(self)
        super().__init__()
        self.timer = GlobalTimer()
        self.assets = AssetManager()
        self.width = width
        self.height = height
        self.title = title
        self.rootAtom = None

        self.__eventDispatcher()

    def init(self):
        builtins.window = self

    def preload(self):
        from p5.core.p5 import sketch as p5sketch

        def resize():
            p5sketch.resized = False
            glfw.set_window_size(p5sketch.window, *p5sketch.size)

        p5sketch.resize = resize

    def setup(self):
        self.assets.load()
        p5.size(self.width, self.height)
        p5.title(self.title)

    def draw(self):
        self.timer.tick()

        p5.background(255)
        res = self.render()
        p5.image(res, 0, 0)

    def render(self):
        return render(self.rootAtom).render()

    def setRoot(self, Atom):
        self.rootAtom = Atom

    def run(self):
        p5.run(
            frame_rate=60,
            sketch_preload=self.preload,
            sketch_draw=self.draw,
            sketch_setup=self.setup,
            renderer="skia",
        )

    def __eventDispatcher(self):
        setattr(
            __main__,
            "mouse_clicked",
            lambda event: self.dispatchEvent(MouseClickedEvent(event, self)),
        )

        setattr(
            __main__,
            "mouse_moved",
            lambda event: self.dispatchEvent(MouseMovedEvent(event, self)),
        )
        setattr(
            __main__,
            "mouse_pressed",
            lambda event: self.dispatchEvent(MousePressedEvent(event, self)),
        )
        setattr(
            __main__,
            "mouse_released",
            lambda event: self.dispatchEvent(MouseReleasedEvent(event, self)),
        )
        setattr(
            __main__,
            "mouse_dragged",
            lambda event: self.dispatchEvent(MouseDraggedEvent(event, self)),
        )
        setattr(
            __main__,
            "mouse_wheel",
            lambda event: self.dispatchEvent(MouseWheelEvent(event, self)),
        )
        setattr(
            __main__,
            "key_pressed",
            lambda event: self.dispatchEvent(KeyPressedEvent(event)),
        )
