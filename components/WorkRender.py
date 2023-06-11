from p5react import *
from p5 import create_graphics, image


def WorkRender(work):
    canvas = useRef(
        ["Work", work.name, "Render", "canvas"],
        work.renderer(),
    )
    buffer = useRef(
        ["Work", work.name, "Render", "buffer"],
        create_graphics(1280, 720),
    )

    def effect():
        canvas = useRef(
            ["Work", work.name, "Render", "canvas"],
            work.renderer(),
        )
        canvas["current"].setup()

        def mousePressed(event):
            canvas["current"].mouse_pressed(event.originalEvent)

        def mouseReleased(event):
            canvas["current"].mouse_released(event.originalEvent)

        def mouseDragged(event):
            canvas["current"].mouse_dragged(event.originalEvent)

        def keyPressed(event):
            canvas["current"].key_pressed(event.originalEvent)

        window.addEventListener("mousePressed", mousePressed)
        window.addEventListener("mouseReleased", mouseReleased)
        window.addEventListener("mouseDragged", mouseDragged)
        window.addEventListener("keyPressed", keyPressed)

        def cleanup():
            window.removeEventListener("mousePressed", mousePressed)
            window.removeEventListener("mouseReleased", mouseReleased)
            window.removeEventListener("mouseDragged", mouseDragged)
            window.removeEventListener("keyPressed", keyPressed)
            canvas["current"].cleanup()

        return cleanup

    useEffect(["Work", work.name, "Render", "init"], effect, [])

    def draw():
        buffer = useRef(
            ["Work", work.name, "Render", "buffer"], create_graphics(1280, 720)
        )
        buffer["current"] = canvas["current"].draw()

    useEffect(["Work", work.name, "Render", "draw"], draw)

    return Graphic(buffer["current"], 0, 0, 1280, 720)
