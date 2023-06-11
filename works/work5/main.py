from ..common.Work import Work
from .renderer import Work5Renderer


class Work5(Work):
    def __init__(self) -> None:
        super().__init__("BallSimulation", "img5.png", "#FFD1D1", Work5Renderer)
