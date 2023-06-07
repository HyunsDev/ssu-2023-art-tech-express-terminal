from p5react import *
from .Title import TitleComponent


class BackgroundComponent(Component):
    def __init__(self, children=None):
        super().__init__(
            0, 0, self.window.width, self.window.height, 0, children=children
        )

        self.x1 = Value(0)
        self.o = Value(0)
        self.x1.transition(100, 60, delay=60)
        self.o.transition(255, 60, delay=60)

    def tick(self):
        super().tick()
        self.x1.tick()
        self.o.tick()

    def render(self):
        return Rect(
            self.x.value,
            self.y.value,
            self.window.width,
            self.window.height,
            style={
                "fill": "#ffffff",
            },
            children=[
                Rect(
                    self.x1.value + 50,
                    50,
                    50,
                    50,
                    style={"fill": "#ff0000", "opacity": self.o.value},
                    children=[Rect(25, 25, 50, 50, style={"fill": "#00ff00"})],
                ),
                TitleComponent(),
            ],
        )
