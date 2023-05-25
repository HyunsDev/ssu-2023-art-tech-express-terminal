from .animatedValue import AnimatedValue

class Area(object):
    def __init__(self, x, y, width, height):
        self.x = AnimatedValue(x)
        self.y = AnimatedValue(y)
        self.width = AnimatedValue(width)
        self.height = AnimatedValue(height)

    def tick(self):
        self.x.tick()
        self.y.tick()
        self.width.tick()
        self.height.tick()

    def transition(self, target, duration, timing):
        self.x.transition(target[0], duration, timing)
        self.y.transition(target[1], duration, timing)
        self.width.transition(target[2], duration, timing)
        self.height.transition(target[3], duration, timing)

    @property
    def hitbox(self):
        return (self.x.value, self.y.value, int(self.width.value), int(self.height.value))
    

