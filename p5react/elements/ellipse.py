import p5
from ..core.element import Element
from ..core.value import Value


__all__ = ["Ellipse"]


class Ellipse(Element):
    name = "ellipse"

    def __init__(
        self,
        x,
        y,
        width,
        height,
        style=None,
        eventListeners={
            "onMouseClick": None,
            "onMouseEnter": None,
            "onMouseLeave": None,
            "oneMousePress": None,
            "onMouseRelease": None,
        },
        children=None,
    ) -> None:
        super().__init__(
            x,
            y,
            width,
            height,
            style=style,
            eventListeners=eventListeners,
            children=children,
        )

    def draw(self, graphic):
        graphic = super().draw(graphic)
        graphic.ellipse(*self.hitbox)
        return graphic
