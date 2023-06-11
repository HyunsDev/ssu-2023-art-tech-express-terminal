__all__ = ["Value", "CubicBezier"]


class CubicBezier:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getPoint(self, t):
        return (
            self.__getCoordinate(t, self.x1, self.x2),
            self.__getCoordinate(t, self.y1, self.y2),
        )

    def __getCoordinate(self, t, p1, p2):
        return 3 * (1 - t) * (1 - t) * t * p1 + 3 * (1 - t) * t * t * p2 + t * t * t


class Value:
    def __init__(self, value) -> None:
        __value = int(value)

        self.initValue = __value
        self.targetValue = __value
        self.__value = __value
        self.time = 0

        self.isPlay = True
        self.duration = 0
        self.timing = None
        self.delay = 0

    @property
    def value(self):
        return self.__value

    def tick(self):
        if not self.isPlay:
            return

        if self.delay > 0:
            self.delay -= 1
            return

        self.time += 1
        if self.time >= self.duration:
            self.isPlay = False
            self.time = self.duration
            self.__value = self.targetValue
        else:
            self.__value = (
                self.timing.getPoint(self.time / self.duration)[1]
                * (self.targetValue - self.initValue)
                + self.initValue
            )

        return self.__value

    def transition(
        self, targetValue, duration, timing=CubicBezier(0, 1, 0, 1), delay=0
    ):
        self.isPlay = True
        self.initValue = self.__value
        self.targetValue = targetValue
        self.duration = duration
        self.delay = delay
        self.time = 0
        if type(timing) == tuple:
            timing = CubicBezier(*timing)
        self.timing = timing

        if duration == 0:
            self.__value = targetValue

    def set(self, value):
        self.isPlay = True
        self.__value = value
        self.initValue = value
        self.targetValue = value
        self.time = 0
