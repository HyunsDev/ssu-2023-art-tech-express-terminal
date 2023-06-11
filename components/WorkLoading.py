from p5react import *
from hooks import useVector
from state import worksScrollState, currentWorkState, routeState


def WorkLoading(work):
    [imagePos, setImagePos] = useVector(
        ["Work", work.name, "img", "pos"], ((1280 - 200) / 2, (720 - 200) / 2)
    )
    [route, setRoute] = useGlobalState(routeState)
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)

    def init2Effect():
        [imagePos, setImagePos] = useVector(
            ["Work", work.name, "img", "pos"], (0, 0), True
        )

        setImagePos(((1280 - 200) / 2, (720 - 200) / 2), 0)
        setImagePos(((1280 - 200) / 2, 800), 20, delay=60, timing=(1, 0, 1, 0))

    useEffect(["Work", work.name, "route"], init2Effect, [route])

    def clickHandler(event):
        [route, setRoute] = useGlobalState(routeState)
        if route == "work":
            setRoute("works")
            setCurrentWork(None)

    def initEffect():
        window.addEventListener("mouseClicked", clickHandler)

        return lambda: resetHook(["Work", work.name])

    useEffect(["Work", work.name, "init"], initEffect, [])

    return Fragment(
        children=[
            Rect(0, 0, 1280, 720, style={"fill": work.color}),
            Image(
                window.assets.getImage(work.image),
                imagePos[0],
                imagePos[1],
                200,
                200,
            ),
        ]
    )
