from ..common.Work import Work
from .renderer import Work2Renderer


class Work2(Work):
    def __init__(self) -> None:
        super().__init__("work1", "img1.png", "#A58660", Work2Renderer)
