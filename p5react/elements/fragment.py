from ..core.element import Element
from ..core.value import Value


class Fragment(Element):
    name = "fragment"

    def __init__(self, children=None) -> None:
        super().__init__(0, 0, 0, 0, children=children)

    def draw(self, graphic):
        graphic = super().draw(graphic)
        return graphic
