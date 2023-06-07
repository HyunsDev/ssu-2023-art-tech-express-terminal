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
        children=None,
    ):
        super().__init__(children)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style
        self.styleParser()

    def styleParser(self):
        if self.style is None:
            self.style = {}
        self.opacity = self.style.get("opacity", 255)
        self.fill = self.style.get("fill", "#f0f0f0")
        self.stroke = self.style.get("stroke", "#f0f0f0")
        self.strokeWeight = self.style.get("strokeWeight", 0)
        self.noStroke = self.style.get("noStroke", True)

    def _render(self):
        self.draw()
        if self.children:
            for child in self.children:
                child.draw()
                child._render()

    def draw(self):
        fillColor = hexToRGB(self.fill)
        p5.fill(*fillColor, self.opacity)
        if self.noStroke:
            p5.no_stroke()
        else:
            p5.stroke_weight(self.strokeWeight)
            p5.stroke(self.stroke)

    @property
    def hitbox(self):
        return (self.x, self.y, self.width, self.height)
