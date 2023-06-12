from p5react import *
from state import currentWorkState


def Title():
    [opacity, transition] = useValue(["Title", "opacity"], 0)
    [subTitleOpacity, transitionSubTitleOpacity] = useValue(
        ["Title", "subtitle", "opacity"], 0
    )
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)

    def WorkEffect():
        [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
        if currentWork != None:
            transitionSubTitleOpacity(255, 30, timing=(0.5, 0.5, 0.5, 0.5), delay=120)
        else:
            transitionSubTitleOpacity(0, 30, timing=(0.5, 0.5, 0.5, 0.5))

    useEffect(["Title", "work"], WorkEffect, [currentWork])

    def effect():
        transition(255, 60, timing=(0, 0, 0, 0), delay=60)

    useEffect(["Title", "init"], effect, [])

    return Text(
        "Express Terminal",
        1280 / 2,
        50,
        textStyle={"size": 20, "align": "CENTER"},
        style={"fill": "#868686", "opacity": opacity},
        children=[
            Text(
                f"{currentWork.name if currentWork != None else ''}",
                1280 / 2,
                72,
                textStyle={"size": 12, "align": "CENTER"},
                style={"fill": "#868686", "opacity": subTitleOpacity},
            )
        ],
    )
