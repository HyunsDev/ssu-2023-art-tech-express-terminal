from ..common.Work import Work
from .renderer import Work4Renderer


class Work4(Work):
    def __init__(self) -> None:
        super().__init__("OwnProcessing", "img4.png", "#000000", Work4Renderer)
