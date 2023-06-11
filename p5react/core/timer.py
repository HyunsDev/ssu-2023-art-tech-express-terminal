__all__ = ["GlobalTimer"]


class GlobalTimer:
    def __init__(self):
        self.time = 0
        self.__symbol = 0
        self.__timers = {}

    def __getSymbol(self):
        self.__symbol += 1
        return self.__symbol - 1

    def setTimeout(self, cb, delay=1):
        symbol = self.__getSymbol()
        _time = self.time + delay
        self.__timers[symbol] = {
            "time": _time,
            "cb": cb,
            "isInterval": False,
        }

        return symbol

    def clearTimeout(self, symbol):
        del self.__timers[symbol]

    def tick(self):
        self.time += 1
        __timers = self.__timers.copy()
        for symbol in __timers:
            timer = __timers[symbol]
            if timer["time"] <= self.time:
                timer["cb"]()
                del self.__timers[symbol]
