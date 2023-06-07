import p5react


class TitleComponent(p5react.Component):
    def __init__(self):
        super().__init__(self.window.width / 2, 50, 0, 0, 30)

        self.o1 = p5react.Value(0)
        self.o1.transition(255, 12, delay=60)

    def tick(self):
        super().tick()
        self.o1.tick()

    def render(self):
        return p5react.Text(
            "Express Terminal",
            x=self.x.value,
            y=self.y.value,
            textStyle={
                "size": 20,
                "font": "NotoSerifKR-Regular",
            },
            style={"opacity": self.o1.value, "fill": "#000000"},
        )
