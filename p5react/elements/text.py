import p5
from ..core.element import Element
from ..core.value import Value


__all__ = ["Text"]


class Text(Element):
    name = "text"

    def __init__(self, text, x, y, textStyle=None, style=None) -> None:
        super().__init__(x, y, style=style)
        self.text = text
        self.font = textStyle.get("font", "NotoSerifKR-Regular")
        self.size = textStyle.get("size", 20)
        self.align = textStyle.get("align", "LEFT")

    def draw(self):
        super().draw()
        p5.text_font(self.window.assets.getFont(self.font))
        p5.text_size(self.size)
        p5.text_align(self.align)
        p5.text(self.text, self.x, self.y)
