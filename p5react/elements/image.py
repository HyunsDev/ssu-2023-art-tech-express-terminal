from p5 import image
from ..core.element import Element
from ..core.value import Value

__all__ = ["Image"]


class Image(Element):
    name = "image"

    def __init__(self, img, x, y, width=None, height=None) -> None:
        super().__init__(x, y)
        self.img = img
        self.x = Value(x)
        self.y = Value(y)
        self.width = Value(width) if width else None
        self.height = Value(height) if height else None

    def draw(self):
        if self.width:
            image(
                self.img,
                self.x.value,
                self.y.value,
                self.width.value,
                self.height.value,
            )
        else:
            image(self.img, self.x.value, self.y.value)
