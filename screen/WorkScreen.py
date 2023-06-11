from p5react import *
from state import currentWorkState
from works import works
from components import WorkLoading, Title, WorkRender, CloseButton


def WorkScreen():
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)

    return Fragment(
        [WorkRender(currentWork), WorkLoading(currentWork), CloseButton(), Title()]
    )
