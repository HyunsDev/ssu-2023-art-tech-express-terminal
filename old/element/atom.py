class Atom(object):
    window = None

    def __init__(self, window=None):
        self.eventListener = {}
        self.timer = {}

        if window:
            Atom.window = window
        self.window = Atom.window

    def addEventListener(self, type, cb):
        if type not in self.eventListener:
            self.eventListener[type] = []
        self.eventListener[type].append(cb)

    def dispatchEvent(self, event):
        self.__dispatchEvent(event.type, event)

    def __dispatchEvent(self, type, event):
        if type in self.eventListener:
            for cb in self.eventListener[type]:
                cb(event)

    def removeEventListener(self, type, cb):
        if type in self.eventListener:
            self.eventListener[type].remove(cb)

    def setTimeout(self, cb, delay=1):
        return self.window.windowTimer.setTimeout(cb, delay)

    def clearTimeout(self, symbol):
        return self.window.windowTimer.clearTimeout(symbol)
