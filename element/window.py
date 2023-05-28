from p5 import *

from element.element import Element
from element.elements import Elements
from element.windowTimer import WindowTimer

from context.p5Context import p5Context
from context.debugContext import debugContext


class Window(Element):
    def __init__(self):
        super().__init__(0, 0, p5Context.width, p5Context.height, window=self)
        self.window = self
        self.elements = Elements()
        self.windowTimer = WindowTimer()

        self.addEventListener("keyPressed", self.__keyPressedHandler)

    def draw(self):
        self.windowTimer.tick()

        super().draw()
        self.elements.draw()

        if debugContext.showHitbox:
            self.__DEBUG_drawHitbox()

    def __DEBUG_drawHitbox(self):
        super().DEBUG_drawHitbox()
        self.elements.DEBUG_drawHitbox()

    def __keyPressedHandler(self, event):
        if event.key == "d":
            self.__debugToggle()

    def __debugToggle(self):
        debugContext.showHitbox = not debugContext.showHitbox
