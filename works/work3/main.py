from ..common.Work import Work
from .renderer import Work3Renderer


class Work3(Work):
    def __init__(self) -> None:
        super().__init__("MergeFunctionsTask", "img3.png", "#E6E6E6", Work3Renderer)
