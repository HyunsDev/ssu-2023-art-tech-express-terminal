from p5react import *
from hooks import useVector
from state import worksScrollState, currentWorkState, routeState, nowActionState


def WorkLoading(work):
    [opacity, transitionOpacity] = useValue(
        ["Work", work.name, "Loading", "opacity"], 255
    )
    [imagePos, setImagePos] = useVector(
        ["Work", work.name, "Loading", "img", "pos"],
        ((1280 - 200) / 2, (720 - 200) / 2),
    )
    [route, setRoute] = useGlobalState(routeState)
    [nowAction, setNowActionState] = useGlobalState(nowActionState)
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)

    def init2Effect():
        [imagePos, setImagePos] = useVector(
            ["Work", work.name, "Loading", "img", "pos"], (0, 0), True
        )

        setImagePos(((1280 - 200) / 2, (720 - 200) / 2), 0)
        setImagePos(((1280 - 200) / 2, 800), 20, delay=60, timing=(1, 0, 1, 0))
        transitionOpacity(0, 20, delay=60, timing=(0.5, 0.5, 0.5, 0.5))

    useEffect(["Work", work.name, "Loading", "route"], init2Effect, [route])

    def closeEffect():
        [nowAction, setNowActionState] = useGlobalState(nowActionState)
        [opacity, transitionOpacity] = useValue(
            ["Work", work.name, "Loading", "opacity"], 255, True
        )

        if nowAction == "close":
            transitionOpacity(255, 40, timing=(1, 0, 1, 0))
            setImagePos(
                ((1280 - 200) / 2, (720 - 200) / 2), 30, delay=30, timing=(0, 1, 0, 1)
            )

            def close():
                setCurrentWork(None)
                setRoute("works")
                setNowActionState("")

            window.setTimeout(close, 80)

    useEffect(["Work", work.name, "Loading", "close"], closeEffect, [nowAction])

    return Fragment(
        children=[
            Rect(0, 0, 1280, 720, style={"fill": work.color, "opacity": opacity}),
            Image(
                window.assets.getImage(work.image),
                imagePos[0],
                imagePos[1],
                200,
                200,
            ),
        ]
    )
