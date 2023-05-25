from p5 import *
from element.element import Element
from element.area import Area
from context.p5Context import p5Context

WORK_SIZE = 200
WORK_GAP = 30
WORK_COUNT = 4


def getX(order, all=WORK_COUNT, gap=WORK_GAP):
    return (p5Context.width / 2 - 100) + ((order) - (all - 1) / 2) * (WORK_SIZE + gap)


class WorkComponent(Element):
    def __init__(self, work, order):
        super().__init__(getX(order), 250, WORK_SIZE, WORK_SIZE, 0)
        self.work = work
        self.order = order
        self.color = self.work.color
        self.isFoucs = False

        self.backgroundArea = Area(getX(order), 250, WORK_SIZE, WORK_SIZE)
        self.imageArea = Area(
            getX(order) + 10, 250 + 10, WORK_SIZE - 20, WORK_SIZE - 20
        )

        self.addEventListener("mousePressed", self.__mousePressedHandler)
        self.addEventListener("mouseOver", self.__mouseOverHandler)
        self.addEventListener("mouseOut", self.__mouseOutHandler)

    def draw(self):
        self.__tick()

        # Background
        noStroke()
        fill(self.color)
        rect(*self.backgroundArea.hitbox)

        # Image
        image(self.work.image, *self.imageArea.hitbox)

    def __tick(self):
        self.backgroundArea.tick()
        self.imageArea.tick()

    def __mousePressedHandler(self, event):
        if self.isFoucs:
            self.__unfocus()
        else:
            self.__focus()

    def __mouseOverHandler(self, event):
        if self.isFoucs:
            return
        self.backgroundArea.transition(
            (self.x - 10, self.y - 10, WORK_SIZE + 20, WORK_SIZE + 20), 12, (0, 1, 0, 1)
        )

    def __mouseOutHandler(self, event):
        if self.isFoucs:
            return
        self.backgroundArea.transition(
            (self.x, self.y, WORK_SIZE, WORK_SIZE), 12, (0, 1, 0, 1)
        )

    def __focus(self):
        self.isFoucs = True
        self.z_index = 100

        backgroundTarget = (0, 0, p5Context.width, p5Context.height)
        self.backgroundArea.transition(backgroundTarget, 12, (0, 1, 0, 1))

        imageTarget = (
            p5Context.width / 2 - WORK_SIZE / 2,
            p5Context.height / 2 - WORK_SIZE / 2,
            WORK_SIZE,
            WORK_SIZE,
        )
        self.imageArea.transition(imageTarget, 10, (0, 1, 0, 1), 2)

        self.x = 0
        self.y = 0
        self.width = p5Context.width
        self.height = p5Context.height

    def __unfocus(self):
        self.isFoucs = False
        self.z_index = 0

        self.backgroundArea.transition(
            (getX(self.order), 250, WORK_SIZE, WORK_SIZE), 12, (0, 1, 0, 1)
        )
        self.imageArea.transition(
            (getX(self.order) + 10, 250 + 10, WORK_SIZE - 20, WORK_SIZE - 20),
            12,
            (0, 1, 0, 1),
        )

        self.x = getX(self.order)
        self.y = 250
        self.width = WORK_SIZE
        self.height = WORK_SIZE
