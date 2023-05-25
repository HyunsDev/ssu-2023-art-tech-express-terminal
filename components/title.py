from p5 import *
from element.element import Element
from context.p5Context import p5Context
from context.assetsContext import assetsContext

class TitleComponent(Element):
    def __init__(self):
        super().__init__(p5Context.width / 2, 20, 0, 0, 100)
        pass
        
    def draw(self):
        fill(0, 0, 0)
        textFont(assetsContext.fonts['NotoSerifKR-Regular'])
        textSize(20)
        text('Express Terminal', self.x, self.y)

        self.width = textWidth('Express Terminal')
        self.height = 20
        self.x = p5Context.width / 2 - self.width / 2
