from p5 import *


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


class AnimatedValue:
    def __init__(self, initValue, returnInt=False) -> None:
        self.initValue = initValue
        self.__value = initValue
        self.returnInt = returnInt

        self.isPlay = False
        self.time = 0

        self.targetValue = None
        self.duration = None
        self.timing = None

        self.delay = 0

    @property
    def value(self):
        if self.returnInt:
            return int(self.__value)
        else:
            return self.__value

    def tick(self):
        if self.isPlay:
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
        pass

    # 현재 값에서 특정 값으로 값을 변화시킵니다.
    def transition(
        self, targetValue, duration, timing=CubicBezier(0.17, 0.67, 0.83, 0.67), delay=0
    ):
        self.time = 0
        self.isPlay = True
        self.initValue = self.value
        self.targetValue = targetValue
        self.duration = duration
        self.delay = delay

        if type(timing) == tuple:
            timing = CubicBezier(*timing)
        self.timing = timing
        pass
