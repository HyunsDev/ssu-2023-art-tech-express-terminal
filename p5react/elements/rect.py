import p5
from ..core.element import Element
from ..core.value import Value


__all__ = ["Rect"]


class Rect(Element):
    name = "rect"

    def __init__(self, x, y, width, height, style=None, children=None) -> None:
        super().__init__(x, y, width, height, style=style, children=children)

    def draw(self):
        super().draw()
        p5.rect(*self.hitbox)
