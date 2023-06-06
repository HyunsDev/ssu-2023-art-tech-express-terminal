class P5Context():
    def __init__(self) -> None:
        self.frameRate = 60
        self.frameCount = 0
        self.width = 1280
        self.height = 720
        pass

p5Context = P5Context()
__all__ = ['p5Context']