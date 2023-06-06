__all__ = ["Atom"]


class Atom(object):
    window = None

    def __init__(self, children=None):
        self.eventListener = {}
        self.timer = {}
        self.children = children
        self.z_index = 0

    def setWindow(self, window):
        Atom.window = window
        self.window = Atom.window

    def draw(self):
        pass

    def tick(self):
        pass

    def render(self):
        pass

    # TODO: 메소드 이름 변경 (기존 render 함수와 혼동 가능성 있음)
    def _render(self):
        pass

    def addEventListener(self, type, cb):
        if type not in self.eventListener:
            self.eventListener[type] = []
        self.eventListener[type].append(cb)

    def dispatchEvent(self, event):
        if event.type in self.eventListener:
            for cb in self.eventListener[event.type]:
                cb(event)

    def removeEventListener(self, type, cb):
        if type in self.eventListener:
            self.eventListener[type].remove(cb)

    def setTimeout(self, cb, delay=1):
        return self.window.windowTimer.setTimeout(cb, delay)

    def clearTimeout(self, symbol):
        return self.window.windowTimer.clearTimeout(symbol)
