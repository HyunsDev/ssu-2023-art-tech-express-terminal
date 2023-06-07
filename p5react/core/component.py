from .atom import Atom
from .value import Value

__all__ = ["Component"]


class Component(Atom):
    def __init__(self, x=0, y=0, width=0, height=0, z_index=0, children=None):
        super().__init__(children)
        self.x = Value(x)
        self.y = Value(y)
        self.width = Value(width)
        self.height = Value(height)
        self.z_index = z_index

    def render(self) -> Atom:
        pass

    def _render(self):
        self.tick()
        element = self.render()
        if element:
            element._render()

    def tick(self):
        self.x.tick()
        self.y.tick()
        self.width.tick()
        self.height.tick()

    @property
    def hitbox(self):
        return (self.x.value, self.y.value, self.width.value, self.height.value)
