from p5react import *
from .LoadingScreen import LoadingScreen
from .WorksScreen import WorksScreen
from .WorkScreen import WorkScreen
from state import routeState, currentWorkState


def Router():
    [route, setRoute] = useGlobalState(routeState)
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)

    ele = Fragment()
    if route == "loading":
        ele = LoadingScreen()
    elif route == "works":
        ele = WorksScreen()
    elif route == "work":
        ele = WorkScreen()

    return Fragment([ele])
