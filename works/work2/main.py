from ..common.Work import Work
from .renderer import Work2Renderer


class Work2(Work):
    def __init__(self) -> None:
        super().__init__("LightScatter", "img2.png", "#000000", Work2Renderer)
