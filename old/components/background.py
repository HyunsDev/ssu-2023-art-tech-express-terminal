from p5 import *
from element.element import Element
from context.p5Context import p5Context


class Background(Element):
    def __init__(self):
        super().__init__(0, 0, p5Context.width, p5Context.height, 0)
        pass

    def draw(self):
        background(255, 255, 255)
