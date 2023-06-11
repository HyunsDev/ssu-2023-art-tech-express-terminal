from p5react import *
from hooks import useVector
from state import worksScrollState, currentWorkState, routeState


def getDefaultPos(order, scroll):
    return (order * 240 + 30 + scroll, 720 / 2 - 110)


def WorkItem(work, order):
    [pos, transitionPos] = useVector(["work", work.name, "pos"], (1280 / 2, 900))
    [size, transitionSize] = useVector(["work", work.name, "size"], (220, 220))
    [opacity, transitionOpacity] = useValue(["work", work.name, "opacity"], 255)
    [scroll, setScroll] = useGlobalState(worksScrollState)
    [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
    [route, setRoute] = useGlobalState(routeState)
    [isCurrent, setIsCurrent] = useState(["work", work.name, "isCurrent"], False)

    # 현재 작업에 반응하는 사이드이펙트
    def currentWorkEffect():
        [pos, transitionPos] = useVector(["work", work.name, "pos"], (1280 / 2, 900))
        [size, transitionSize] = useVector(["work", work.name, "size"], (220, 220))
        [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
        [isCurrent, setIsCurrent] = useState(["work", work.name, "isCurrent"], False)
        [scroll, setScroll] = useGlobalState(worksScrollState)

        if currentWork == work:
            return
        elif currentWork == None:
            if isCurrent:
                transitionPos(getDefaultPos(order, scroll), 30)
                transitionSize((220, 220), 30)
                setIsCurrent(False)
            else:
                transitionOpacity(0, 20, delay=order * 3, timing=(0.5, 0.5, 0.5, 0.5))
        else:
            transitionOpacity(
                255, 20, delay=20 + order * 3, timing=(0.5, 0.5, 0.5, 0.5)
            )

    useEffect(["work", work.name, "currentWork"], currentWorkEffect, [currentWork])

    # 스크롤에 반응하는 사이드이펙트
    def scrollEffect():
        transitionPos(getDefaultPos(order, scroll), 1, timing=(0.5, 0.5, 0.5, 0.5))

    useEffect(["work", work.name, "scroll"], scrollEffect, [scroll])

    # 클릭에 반응하는 사이드이펙트
    def clickHandler(event):
        [size, transitionSize] = useVector(["work", work.name, "size"], (220, 220))
        [pos, transitionPos] = useVector(["work", work.name, "pos"], (1280 / 2, 900))
        [scroll, setScroll] = useGlobalState(worksScrollState)
        [currentWork, setCurrentWork] = useGlobalState(currentWorkState)
        [route, setRouter] = useGlobalState(routeState)

        if pos[0] < event.x < pos[0] + size[0] and pos[1] < event.y < pos[1] + size[1]:
            if currentWork == work:
                return

            elif currentWork == None:
                [scrollValue, setScrollValue] = useValue(
                    ["WorksScreen", "scroll"], scroll, True
                )

                setIsCurrent(True)
                setCurrentWork(work)

                setScrollValue(scroll, 0)
                setScrollValue(
                    1280 / 2 - size[0] / 2 - (order * 240 + 30),
                    60,
                )
                transitionPos((1280 / 2 - size[0] / 2, 720 / 2 - size[1] / 2), 30)

                window.setTimeout(
                    lambda: transitionSize(
                        (210, 210), 15, timing=(0.25, 0.75, 0.25, 0.75)
                    ),
                    66,
                )
                window.setTimeout(
                    lambda: transitionPos(
                        (1280 / 2 - size[0] / 2 + 5, 720 / 2 - size[1] / 2 + 5),
                        15,
                        timing=(0.25, 0.75, 0.25, 0.75),
                    ),
                    66,
                )

                window.setTimeout(
                    lambda: transitionPos(
                        (0, 0),
                        30,
                    ),
                    81,
                )
                window.setTimeout(
                    lambda: transitionSize(
                        (1280, 720),
                        30,
                    ),
                    81,
                )

                window.setTimeout(lambda: setRouter("work"), 111)

    # 클릭 및 초기화
    def effect():
        window.addEventListener("mouseClicked", clickHandler)
        transitionPos(getDefaultPos(order, scroll), 60, delay=order * 12)
        transitionOpacity(0, 60, delay=order * 12)

    useEffect(["work", work.name, "iniit"], effect, [])

    textOpacity = 280 - abs(pos[0] + size[0] / 2 - 1280 / 2)

    children = [
        Text(
            f"{work.name}",
            pos[0] + size[0] / 2,
            pos[1] + size[1] / 2 + 150,
            textStyle={"size": 20, "align": "CENTER"},
            style={
                "fill": "#000000",
                "opacity": textOpacity * (255 - opacity) / 255,
            },
        ),
        Rect(
            pos[0],
            pos[1],
            size[0],
            size[1],
            style={
                "fill": work.color,
            },
        ),
        Image(
            window.assets.getImage(work.image),
            (pos[0] + (size[0] - 200) / 2),
            (pos[1] + (size[1] - 200) / 2),
            200,
            200,
        ),
        Rect(
            pos[0],
            pos[1],
            size[0],
            size[1],
            style={
                "fill": "#ffffff",
                "opacity": opacity,
            },
        ),
    ]

    return Fragment(children)
