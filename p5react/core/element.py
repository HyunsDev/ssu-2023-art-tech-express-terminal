from p5 import *
from .atom import Atom

__all__ = ["Element"]


class Element(Atom):
    name = "element"

    def __init__(self, x, y, children=None):
        super().__init__(children)
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

    def _render(self):
        self.draw()
        if self.children:
            for child in self.children:
                child.draw()
                child._render()

    @property
    def hitbox(self):
        return (self.x, self.y, self.width, self.height)
