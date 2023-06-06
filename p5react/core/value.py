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

        self.isPuase = False
        self.duration = None
        self.timing = None
        self.deplay = 0

    @property
    def value(self):
        return self.__value

    def tick(self):
        if self.isPuase:
            return

        if self.deplay > 0:
            self.deplay -= 1
            return

        self.time += 1
        if self.time >= self.duration:
            self.time = self.duration
            self.__value = self.targetValue
        else:
            self.__value = (
                self.timing.getPoint(self.time / self.duration)[1]
                * (self.targetValue - self.initValue)
                + self.initValue
            )

    def transition(
        self, targetValue, duration, timing=CubicBezier(0, 1, 1, 0), deplay=0
    ):
        self.initValue = self.__value
        self.targetValue = targetValue
        self.duration = duration
        self.timing = timing
        self.deplay = deplay
        self.time = 0
        self.isPuase = False
        if type(timing) == tuple:
            timing = CubicBezier(*timing)

    def set(self, value):
        self.__value = value
        self.initValue = value
        self.targetValue = value
        self.time = 0
        self.isPuase = False
