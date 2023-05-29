from p5 import *
from element.element import Element
from context.p5Context import p5Context
from context.assetsContext import assetsContext
from utils import hexToRGB

from element.animatedValue import AnimatedValue


class AnimatedText(Element):
    def __init__(
        self,
        text,
        x: int = 0,
        y: int = 0,
        color="#000000",
        size=20,
        align="LEFT",
        opacity=1,
        font="NotoSerifKR-Regular",
        z_index: int = 0,
    ):
        self.font = font
        self.text = text
        self.size = size
        self.align = align
        self.color = hexToRGB(color)
        self._opacity = AnimatedValue(opacity)
        self._x = AnimatedValue(x)
        self._y = AnimatedValue(y)

        super().__init__(x, y, self.getTextWidth(), self.size, z_index)

    def getTextWidth(self):
        text_font(assetsContext.fonts[self.font])
        text_size(self.size)
        text_align(self.align)
        return text_width(self.text)

    def draw(self):
        self.__tick()
        if self.align == "CENTER":
            self.x = self._x.value - self.getTextWidth() / 2
        else:
            self.x = self._x.value
        self.y = self._y.value

        fill(*self.color, self._opacity.value)
        text_font(assetsContext.fonts[self.font])
        text_size(self.size)
        text_align(self.align)
        text(self.text, self._x.value, self._y.value)

    def __tick(self):
        self._x.tick()
        self._y.tick()
        self._opacity.tick()

    def move(self, x, y, duration=12, timing=(0, 1, 0, 1), delay=0):
        self._x.transition(x, duration, timing, delay)
        self._y.transition(y, duration, timing, delay)

    def fade(self, opacity, duration=12, timing=(0, 1, 0, 1), delay=0):
        self._opacity.transition(opacity, duration, timing, delay)
