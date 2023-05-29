from p5 import *
from element.element import Element
from context.p5Context import p5Context
from .animatedText import AnimatedText
from element.animatedValue import AnimatedValue

from components import TitleComponent, WorkComponent, FooterComponent
from works.work1.main import Work1


class LoadingScreen(Element):
    def __init__(self):
        super().__init__(0, 0, p5Context.width, p5Context.height, 0)

        self.loading = AnimatedValue(0, returnInt=True)
        self.loading.transition(100, 90, (0.5, 0.5, 0.5, 0.5), delay=12)

        self.loadingText = AnimatedText(
            "Loading 0%",
            p5Context.width / 2,
            p5Context.height / 2 - 30,
            color="#000000",
            size=12,
            align="CENTER",
            opacity=0,
            z_index=100,
        )
        self.loadingText.fade(255, 12, (0.5, 0.5, 0.5, 0.5), delay=12)

        self.window.elements.append(self.loadingText)

        self.setTimeout(self.__fadeOut, 135)

    def draw(self):
        self.__tick()
        background(255, 255, 255)

    def __tick(self):
        self.loading.tick()
        self.loadingText.text = f"Loading {self.loading.value}%"

    def __fadeOut(self):
        self.loadingText.fade(0, 30, (0.5, 0.5, 0.5, 0.5))
        self.setTimeout(self.__showWorks, 30)

    def __showWorks(self):
        self.window.elements.append(TitleComponent())
        self.window.elements.append(FooterComponent())
        self.window.elements.append(WorkComponent(Work1(), 0))
        self.window.elements.append(WorkComponent(Work1(), 1))
        self.window.elements.append(WorkComponent(Work1(), 2))
        self.window.elements.append(WorkComponent(Work1(), 3))
