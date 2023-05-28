from context.p5Context import p5Context


class WindowTimer:
    def __init__(self):
        # [{ time: number, cb: func, isInterval: boolean, interval: number }]
        self.__symbol = 0
        self.__timers = {}

    def __getSymbol(self):
        self.__symbol += 1
        return self.__symbol - 1

    def setTimeout(self, cb, delay=1):
        symbol = self.__getSymbol()
        _time = p5Context.frameCount + delay
        self.__timers[symbol] = {
            "time": _time,
            "cb": cb,
            "isInterval": False,
        }

        return symbol

    def clearTimeout(self, symbol):
        del self.__timers[symbol]

    def tick(self):
        p5Context.frameCount += 1

        __timers = self.__timers.copy()
        for symbol in __timers:
            timer = __timers[symbol]
            if timer["time"] <= p5Context.frameCount:
                print(timer["time"])
                timer["cb"]()
                del self.__timers[symbol]
