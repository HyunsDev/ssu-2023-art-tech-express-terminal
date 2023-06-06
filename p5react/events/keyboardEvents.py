from .event import Event

__all__ = (
    "KeyboardEvent",
    "KeyPressedEvent",
)


class KeyboardEvent(Event):
    def __init__(self, event):
        super().__init__()
        self.key = event.key


class KeyPressedEvent(KeyboardEvent):
    def __init__(self, event):
        super().__init__(event)
        self.type = "keyPressed"
