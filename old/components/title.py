from p5 import *
from .animatedText import AnimatedText

from context.p5Context import p5Context


class TitleComponent(AnimatedText):
    def __init__(self):
        super().__init__(
            "Express Terminal",
            p5Context.width / 2,
            30,
            color="#000000",
            size=20,
            align="CENTER",
            opacity=0,
            z_index=100,
        )

        self._opacity.transition(255, 12, (0.5, 0.5, 0.5, 0.5), delay=60)
