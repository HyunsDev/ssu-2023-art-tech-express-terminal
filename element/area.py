from .animatedValue import AnimatedValue


class Area(object):
    def __init__(self, x, y, width, height):
        self.x = AnimatedValue(x, returnInt=True)
        self.y = AnimatedValue(y, returnInt=True)
        self.width = AnimatedValue(width, returnInt=True)
        self.height = AnimatedValue(height, returnInt=True)

    def tick(self):
        self.x.tick()
        self.y.tick()
        self.width.tick()
        self.height.tick()

    def transition(self, target, duration, timing, delay=0):
        self.x.transition(target[0], duration, timing, delay)
        self.y.transition(target[1], duration, timing, delay)
        self.width.transition(target[2], duration, timing, delay)
        self.height.transition(target[3], duration, timing, delay)

    @property
    def hitbox(self):
        return (
            self.x.value,
            self.y.value,
            int(self.width.value),
            int(self.height.value),
        )
