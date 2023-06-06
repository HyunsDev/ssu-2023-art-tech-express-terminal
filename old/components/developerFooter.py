from p5 import *
from .animatedText import AnimatedText

from context.p5Context import p5Context


class FooterComponent(AnimatedText):
    def __init__(self):
        super().__init__(
            "Hyuns Yuna Ngg",
            p5Context.width / 2,
            p5Context.height - 50,
            color="#000000",
            size=12,
            align="CENTER",
            opacity=0,
            font="NotoSansKR-Regular",
            z_index=100,
        )

        self._opacity.transition(255, 12, (0.5, 0.5, 0.5, 0.5), delay=60)

        self.addEventListener("mouseOver", self.__mouseOverHandler)
        self.addEventListener("mouseOut", self.__mouseOutHandler)

    def tick(self):
        self._opacity.tick()

    def __mouseOverHandler(self, event):
        self._opacity.transition(200, 12, (0.5, 0.5, 0.5, 0.5))

    def __mouseOutHandler(self, event):
        self._opacity.transition(255, 12, (0.5, 0.5, 0.5, 0.5))
