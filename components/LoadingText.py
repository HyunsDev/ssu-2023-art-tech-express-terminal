from p5react import useEffect, useValue, Text


def LoadingText():
    [loading, moveLoading] = useValue(["LT", "loading"], 0)
    [opacity, moveOpacity] = useValue(["LT", "opacity"], 0)

    def effect():
        moveLoading(100, 120, timing=(0.5, 0.5, 0.5, 0.5))
        moveOpacity(255, 60, timing=(0.5, 0.5, 0.5, 0.5))
        window.setTimeout(lambda: moveOpacity(0, 60, timing=(0.5, 0.5, 0.5, 0.5)), 180)

    useEffect("lt", effect, [])

    return Text(
        f"Loading... {int(loading)}%",
        1280 / 2,
        720 / 2,
        textStyle={"size": 12, "align": "CENTER"},
        style={"fill": "#000000", "opacity": opacity},
    )
