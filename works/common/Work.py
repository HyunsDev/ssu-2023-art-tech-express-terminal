from p5react import *
from p5 import graphics


class Work(Atom):
    name: str
    image: str
    color: str

    def __init__(self, name: str, image: str, color: str, renderer) -> None:
        super().__init__()
        self.name = name
        self.image = image
        self.color = color
        self.renderer = renderer

    def setup(self):
        pass

    def draw(self):
        pass
