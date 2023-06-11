from p5 import image, create_graphics
from ..core.element import Element
from ..core.value import Value
from ..utils import hexToRGB


class Graphic(Element):
    name = "graphic"

    def __init__(self, buffer, x, y, width=1280, height=720, style=None, children=None):
        super().__init__(x, y, width, height, style=style, children=children)
        self.buffer = buffer

    def draw(self, graphic):
        graphic = super().draw(graphic)
        graphic.image(self.buffer, *self.hitbox)
        return graphic
