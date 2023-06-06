import p5
from ..core.element import Element
from ..core.value import Value


__all__ = ["Rect"]


class Rect(Element):
    name = "rect"

    def __init__(self, x, y, width, height, color="#ffffff", children=None) -> None:
        super().__init__(x, y, children)
        self.x = Value(x)
        self.y = Value(y)
        self.width = Value(width)
        self.height = Value(height)
        self.color = color

    def draw(self):
        p5.fill(self.color)
        p5.rect(self.x.value, self.y.value, self.width.value, self.height.value)
