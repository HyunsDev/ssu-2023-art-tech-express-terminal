from .event import Event

class MouseEvent(Event):
    def __init__(self, event, target):
        self.type = 'mouse'
        self.originalEvent = event
        self.x = event.x
        self.y = event.y
        self.button = event.button
        self.pressed = event.pressed
        self.target = target

class MouseClickedEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseClicked'

class MouseMovedEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseMoved'

class MouseOverEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseOver'

class MouseOutEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseOut'

class MousePressedEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mousePressed'

class MouseReleasedEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseReleased'

class MouseDraggedEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseDragged'

class MouseWheelEvent(MouseEvent):
    def __init__(self, event, target):
        super().__init__(event, target)
        self.type = 'mouseWheel'
