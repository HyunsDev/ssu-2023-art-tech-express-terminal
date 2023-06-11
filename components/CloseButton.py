from p5react import *
from hooks import useVector
from state import worksScrollState, currentWorkState, routeState, nowActionState


def CloseButton():
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
    [nowAction, setNowAction] = useGlobalState(nowActionState)
    [posX, transitionPosX] = useValue(["closeButton", "posX"], 1280 + 75)

    def currentWorkEffect():
        [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
        [posX, transitionPosX] = useValue(["closeButton", "posX"], 1280 + 75, True)

        if currentWork == None:
            transitionPosX(1280 + 75, 20, timing=(1, 0, 1, 0))
        else:
            transitionPosX(1280 - 75, 20, delay=180, timing=(0, 1, 0, 1))

    useEffect(["closeButton", "currentWork"], currentWorkEffect, [currentWork])

    def effect():
        def mousePressedHandler(event):
            [posX, transitionPosX] = useValue(["closeButton", "posX"], 1280 + 75)
            [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
            [route, setRoute] = useGlobalState(routeState)

            if posX < event.x < posX + 50 and 720 / 2 - 25 < event.y < 720 / 2 + 25:
                if currentWork != None:
                    setNowAction("close")

        window.addEventListener("mousePressed", mousePressedHandler)

        def cleanup():
            window.removeEventListener("mousePressed", mousePressedHandler)

        return cleanup

    useEffect(["closeButton", "init"], effect, [])

    return Image(
        window.assets.getImage("x.png"),
        posX,
        720 / 2 - 25,
        50,
        50,
    )
