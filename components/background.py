from p5react import *


class BackgroundComponent(Component):
    def __init__(self, children=None):
        super().__init__(0, 0, self.window.width, self.window.height, 0)

    def render(self):
        return Rect(
            0,
            0,
            self.window.width,
            self.window.height,
            "#ffffff",
            children=[
                Rect(
                    50,
                    50,
                    50,
                    50,
                    "#ff0000",
                    children=[Rect(25, 25, 50, 50, "#00ff00")],
                ),
            ],
        )
