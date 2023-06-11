from p5react import *
from state import currentWorkState
from works import works
from components import WorkLoading, Title


def WorkScreen():
    [currentWorks, setCurrentWork] = useGlobalState(currentWorkState)

    return Fragment([WorkLoading(currentWorks), Title()])
