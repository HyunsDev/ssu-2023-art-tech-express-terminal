from .atom import Atom

__all__ = ["Component"]


class Component(Atom):
    def __init__(self, x=0, y=0, width=0, height=0, z_index=0, children=None):
        super().__init__(children)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z_index = z_index

    def _render(self):
        element = self.render()
        if element:
            element._render()

    @property
    def hitbox(self):
        return (self.x, self.y, self.width, self.height)
