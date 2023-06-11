from ..common.Work import Work


class Renderer:
    pass


class Work1(Work):
    def __init__(self) -> None:
        super().__init__("work1", "img1.png", "#A58660", Renderer)
