from p5react import *


def useVector(key, pos, noTick=False):
    [x, transX] = useValue([*key, "useVector", "x"], pos[0], noTick)
    [y, transY] = useValue([*key, "useVector", "y"], pos[1], noTick)

    def transition(vector, duration, timing=(0, 1, 0, 1), delay=0):
        transX(vector[0], duration, timing, delay)
        transY(vector[1], duration, timing, delay)

    return [(x, y), transition]
