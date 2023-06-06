from p5 import *
from element.element import Element
from context.p5Context import p5Context
from components import WorkComponent
from works.work1.main import Work1


class WorksComponent(Element):
    def __init__(self):
        super().__init__(0, 0, p5Context.width, p5Context.height, 0)

        self.works = []
        self.addWork(Work1())
        self.addWork(Work1())
        self.addWork(Work1())
        self.addWork(Work1())
        self.addWork(Work1())
        self.addWork(Work1())

        self.worksScrollState = 0

        self.window.addEventListener("mouseWheel", self.__mouseWheelEventHandler)

    def addWork(self, work):
        workComponent = WorkComponent(work, len(self.works))
        self.works.append(workComponent)
        self.window.elements.append(workComponent)

    def draw(self):
        super().draw()

    def __mouseWheelEventHandler(self, event):
        self.worksScrollState += event.scroll.x
