from p5 import image
from ..core.element import Element
from ..core.value import Value
from ..utils import hexToRGB

__all__ = ["Image"]


class Image(Element):
    name = "image"

    def __init__(
        self,
        img,
        x,
        y,
        width=None,
        height=None,
        imageStyle=None,
        style=None,
        children=None,
    ) -> None:
        super().__init__(x, y, width, height, style=style, children=children)
        self.img = img

        if (imageStyle) is None:
            imageStyle = {}

        self.tintColor = None
        if imageStyle.get("tintColor", None) is not None:
            self.tintColor = hexToRGB(imageStyle.get("tintColor", None))
        self.tintOpacity = imageStyle.get("tintOpacity", None)

    def draw(self, graphic):
        graphic = super().draw(graphic)
        if (self.tintColor and self.tintOpacity) is not None:
            graphic.tint(*self.tintColor, self.tintOpacity)
        graphic.image(self.img, *self.hitbox)
        return graphic
