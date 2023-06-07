from p5 import image
from ..core.element import Element
from ..core.value import Value

__all__ = ["Image"]


class Image(Element):
    name = "image"

    def __init__(self, img, x, y, width=None, height=None, style=None) -> None:
        super().__init__(x, y, width, height, style=style)
        self.img = img

    def draw(self):
        image(
            self.img,
            self.x.value,
            self.y.value,
            self.width,
            self.height,
        )
