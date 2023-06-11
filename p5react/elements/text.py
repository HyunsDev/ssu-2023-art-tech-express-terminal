import p5
from ..core.element import Element
from ..core.value import Value


__all__ = ["Text"]


class Text(Element):
    name = "text"

    def __init__(self, text, x, y, textStyle=None, style=None, children=None) -> None:
        super().__init__(x, y, style=style)
        self.text = text
        self.font = textStyle.get("font", "NotoSerifKR-Regular")
        self.size = textStyle.get("size", 20)
        self.align = textStyle.get("align", "LEFT")
        self.children = children

    def draw(self, graphic):
        graphic = super().draw(graphic)
        graphic.text_font(self.window.assets.getFont(self.font))
        graphic.text_size(self.size)
        graphic.text_align(self.align)
        graphic.text(self.text, self.x, self.y)
        return graphic
