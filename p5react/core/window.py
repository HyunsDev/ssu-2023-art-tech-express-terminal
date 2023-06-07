from .atom import Atom
from .timer import GlobalTimer
from ..events import *
from .assetManager import AssetManager
import p5
import __main__

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

    def setup(self):
        self.assets.load()
        p5.size(self.width, self.height)
        p5.title(self.title)

    def draw(self):
        self.timer.tick()
        self._render()

    def render(self):
        return self.rootAtom

    def _render(self):
        element = self.render()
        if element:
            element._render()

    def setRoot(self, Atom):
        self.rootAtom = Atom

    def run(self):
        p5.run(frame_rate=60, sketch_draw=self.draw, sketch_setup=self.setup)

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
