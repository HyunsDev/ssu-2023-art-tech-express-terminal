from p5 import *

pg = None


def setup():
    global pg
    size(710, 400)
    pg = create_graphics(400, 250)


def draw():
    background(255)

    fill(0, 12)
    rect(0, 0, width, height)
    fill(255)
    no_stroke()
    ellipse(mouse_x, mouse_y, 60, 60)

    pg.background(51)
    pg.no_fill()
    pg.stroke(255)
    pg.ellipse(mouse_x - 150, mouse_y - 75, 60, 60)

    # Draw the offscreen buffer to the screen with image()
    image(pg, 150, 75)


if __name__ == "__main__":
    # Create Graphics is only available in skia
    run(renderer="skia")
