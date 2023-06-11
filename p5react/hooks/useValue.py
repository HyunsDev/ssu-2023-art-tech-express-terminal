from ..core.value import Value, CubicBezier
from ..core.p5react import useEffect, useState, useRef


def useValue(key, initialValue, noTick=False):
    [value, setValue] = useState([*key, "useValue"], Value(initialValue))

    if not noTick:
        value.tick()

    def transition(targetValue, duration, timing=CubicBezier(0, 1, 0, 1), delay=0):
        value.transition(targetValue, duration, timing, delay)

    return [value.value, transition]
