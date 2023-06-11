from p5react import *
from components.LoadingText import LoadingText
from state import routeState


def LoadingScreen():
    [isShow, setIsShow] = useState(["loading"], False)
    [route, setRouter] = useGlobalState(routeState)

    def move():
        setRouter("works")

    def effect():
        window.setTimeout(lambda: setIsShow(True), 30)
        window.setTimeout(move, 300)

    useEffect("loading", effect, [])

    if isShow:
        return LoadingText()
    else:
        return Fragment()
