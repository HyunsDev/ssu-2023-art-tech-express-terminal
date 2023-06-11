from ..common.Work import Work
from .renderer import Work6Renderer


class Work6(Work):
    def __init__(self) -> None:
        super().__init__("Pixelation", "img6.png", "#B9613B", Work6Renderer)
