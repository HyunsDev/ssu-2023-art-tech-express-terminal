import p5
from .atom import Atom
from ..utils import hexToRGB
from .value import Value

__all__ = ["Element"]


class Element(Atom):
    name = "element"

    def __init__(
        self,
        x,
        y,
        width=0,
        height=0,
        style=None,
        eventListeners={
            "onMouseClick": None,
            "onMouseEnter": None,
            "onMouseLeave": None,
            "oneMousePress": None,
            "onMouseRelease": None,
        },
        children=None,
    ):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style
        self.children = children
        self.styleParser()

    def styleParser(self):
        if self.style is None:
            self.style = {}
        self.opacity = self.style.get("opacity", 255)
        self.fill = self.style.get("fill", "#f0f0f0")
        self.stroke = self.style.get("stroke", "#f0f0f0")
        self.strokeWeight = self.style.get("strokeWeight", 0)
        self.noStroke = self.style.get("noStroke", True)

    def render(self, graphic=None):
        if not graphic:
            graphic = p5.create_graphics(self.window.width, self.window.height)

        graphic = self.draw(graphic)

        if self.children:
            for child in self.children:
                graphic = child.render(graphic)

        return graphic

    def draw(self, graphic):
        fillColor = hexToRGB(self.fill)
        graphic.fill(*fillColor, self.opacity)
        if self.noStroke:
            graphic.no_stroke()
        else:
            graphic.stroke_weight(self.strokeWeight)
            graphic.stroke(self.stroke)
        return graphic

    @property
    def hitbox(self):
        return (self.x, self.y, self.width, self.height)
