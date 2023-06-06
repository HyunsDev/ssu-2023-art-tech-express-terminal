from .atom import Atom
from p5 import *
from event import MouseOverEvent, MouseOutEvent


class Element(Atom):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        z_index: int = 0,
        window=None,
    ):
        super().__init__(window)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z_index = z_index

        self.isMouseOver = False

        self.window.addEventListener("mousePressed", self.__mousePressedHandler)
        self.window.addEventListener("mouseMoved", self.__mouseMoved)

    def draw(self):
        self.tick()
        pass

    def tick(self):
        pass

    def getHithox(self):
        return (self.x, self.y, self.width, self.height)

    def __isInHitbot(self, x, y):
        hitbox = self.getHithox()
        return (
            hitbox[0] <= x <= hitbox[0] + hitbox[2]
            and hitbox[1] <= y <= hitbox[1] + hitbox[3]
        )

    def DEBUG_drawHitbox(self):
        noFill()
        stroke(255, 0, 0)
        strokeWeight(1)
        rect(*self.getHithox())

    def __mousePressedHandler(self, event):
        if event.target != self and self.__isInHitbot(event.x, event.y):
            self.dispatchEvent(event)

    def __mouseMoved(self, event):
        if event.target != self:
            if self.__isInHitbot(event.x, event.y) and not self.isMouseOver:
                self.isMouseOver = True
                self.dispatchEvent(MouseOverEvent(event, self))
            elif not self.__isInHitbot(event.x, event.y) and self.isMouseOver:
                self.isMouseOver = False
                self.dispatchEvent(MouseOutEvent(event, self))
