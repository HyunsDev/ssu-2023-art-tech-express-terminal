from p5 import text
from ..core.element import Element
from ..core.value import Value


__all__ = ["Text"]


class Text(Element):
    name = "text"

    def __init__(self, text, x, y) -> None:
        super().__init__(x, y)
        self.text = text
        self.x = Value(x)
        self.y = Value(y)

    def draw(self):
        text(self.text.value, self.x.value, self.y.value)
