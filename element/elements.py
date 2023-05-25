class Elements:
    def __init__(self) -> None:
        self.elements = []

    def draw(self):
        self.elements = sorted(self.elements, key=lambda element: element.z_index)

        for element in self.elements:
            element.draw()

    def DEBUG_drawHitbox(self):
        for element in self.elements:
            element.DEBUG_drawHitbox()

    def append(self, element):
        self.elements.append(element)
        
    def remove(self, element):
        self.elements.remove(element)