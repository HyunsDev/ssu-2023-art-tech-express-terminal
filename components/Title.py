from p5react import *


def Title():
    [opacity, transition] = useValue(["Title"], 0)

    def effect():
        transition(255, 60, timing=(0, 0, 0, 0), delay=60)

    useEffect(["Title"], effect, [])

    return Text(
        "Express Terminal",
        1280 / 2,
        50,
        textStyle={"size": 20, "align": "CENTER"},
        style={"fill": "#000000", "opacity": opacity},
    )
