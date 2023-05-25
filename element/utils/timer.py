from context.p5Context import p5Context

class Timer:
    def __init__(self):
        # [{ time: number, cb: func, isInterval: boolean, interval: number }]
        self.__symbol = 0
        self.__timers = {}

    def __getSymbol(self):
        self.__symbol += 1
        return self.__symbol - 1

    def setTimeout(self, cb, delay=1):
        symbol = self.__getSymbol()
        _time = p5Context.frameCount + delay * p5Context.frameRate
        self.__timers[symbol] = {
            "time": _time,
            "cb": cb,
            "isInterval": False,
        }
        return symbol

    def clearTimeout(self, symbol):
        del self.__timers[symbol]

    def tick(self):
        for symbol in self.__timers:
            timer = self.__timers[symbol]
            if timer["time"] <= p5Context.frameCount:
                timer["cb"]()
                del self.__timers[symbol]
