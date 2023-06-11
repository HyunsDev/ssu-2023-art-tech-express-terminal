from p5react import *
from works import works
from components import WorkItem, Title, CloseButton
from state import worksScrollState, currentWorkState


def getWorks(currentWork=None):
    [lastCurrentWork, setLastCurrentWork] = useState("lastCurrentWork", None)

    def effect():
        if currentWork == None:
            return
        setLastCurrentWork(currentWork)

    useEffect("lastCurrentWork", effect, [currentWork])

    workItems = []
    for work in works:
        if lastCurrentWork == work:
            continue
        workItems.append(WorkItem(work, works.index(work)))

    if lastCurrentWork != None:
        workItems.append(WorkItem(lastCurrentWork, works.index(lastCurrentWork)))

    return workItems


def WorksScreen():
    [scroll, setScroll] = useGlobalState(worksScrollState)
    [currentWorks, setCurrentWork] = useGlobalState(currentWorkState)

    [scrollValue, setScrollValue] = useValue(["WorksScreen", "scroll"], scroll)

    def scrollValueEffect():
        [scrollValue, setScrollValue] = useValue(["WorksScreen", "scroll"], 0)
        setScroll(scrollValue)

    useEffect(["WorksScreen", "scroll"], scrollValueEffect, [scrollValue])

    def scrollHandler(event):
        [currentWorks, setCurrentWork] = useGlobalState(currentWorkState)
        if currentWorks == None:
            setScroll(lambda scroll: scroll + (event.scroll.x - event.scroll.y) * 2)

    def effect():
        window.addEventListener("mouseWheel", scrollHandler)

    useEffect("works", effect, [])

    return Fragment(
        children=[
            Fragment(getWorks(currentWorks)),
            CloseButton(),
            Title(),
        ]
    )
