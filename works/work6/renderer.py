from ..common import Renderer
from p5 import create_graphics, load_image
from collections import Counter

width, height = 1280, 720


class node:
    def __init__(self, left_topX, left_topY, avgcolor, Length, Height):
        self.x = left_topX
        self.y = left_topY
        self.avgcolor = avgcolor
        self.l = Length
        self.h = Height

    def draw(self, graphic):
        graphic.fill(*self.avgcolor)
        graphic.rect(self.x, self.y, self.l, self.h)
        return graphic


class Work6Renderer(Renderer):
    def setup(self):
        self.nodes_list = [[]]
        self.colors_dict = {}
        self.nodesize = 8
        self.pixels_list = [[]]
        self.start = True
        self.isdraw = False
        self.startX = 0
        self.startY = 0
        self.worksize = 500
        self.EndX = self.startX + self.worksize
        self.EndY = self.startY + self.worksize

        self.image = load_image("works/work6/scream.png")

        self.graphic = create_graphics(width, height)

    def draw(self):
        self.graphic.no_stroke()

        if self.start:
            self.graphic.background(255)
            self.graphic.image(
                self.image,
                1280 / 2 - self.worksize / 2,
                720 / 2 - self.worksize / 2,
            )
            self.loadimage()

            self.start = False

        if self.isdraw:
            self.graphic.fill(255)
            self.graphic.rect(
                self.startX, self.startY, self.worksize, self.worksize + 101
            )
            self.nodes_list = [[] for _ in range(width // self.nodesize)]
            self.calculate(self.nodesize)
            for x in range(self.startX, self.EndX, self.nodesize):
                for y in range(self.startY, self.EndY, self.nodesize):
                    if x + self.nodesize > self.EndX:
                        x = self.EndX - self.nodesize
                    if y + self.nodesize > self.EndY:
                        y = self.EndY - self.nodesize
                    node_color = self.colors_dict[self.nodesize][(x, y)]
                    self.nodes_list[x // self.nodesize].append(
                        node(
                            x + 1280 / 2 - self.worksize / 2,
                            y + 720 / 2 - self.worksize / 2,
                            node_color,
                            self.nodesize,
                            self.nodesize,
                        )
                    )
                    self.graphic = self.nodes_list[x // self.nodesize][-1].draw(
                        self.graphic
                    )

            self.isdraw = False

        return self.graphic

    def loadimage(self):
        self.pixels_list = [[0 for _ in range(height)] for _ in range(width)]
        self.image.load_pixels()
        for x in range(self.startX, self.EndX):
            for y in range(self.startY, self.EndY):
                index = (x, y)
                print(index)

                p = self.image.pixels[index]
                a = (int(p[0]), int(p[1]), int(p[2]))
                self.pixels_list[x][y] = a
        self.image.update_pixels()

    def calculate(self, node_size):
        self.colors_dict = {}
        for x in range(self.startX, self.EndX, node_size):
            for y in range(self.startY, self.EndY, node_size):
                colors_list = []
                if x + self.nodesize > self.EndX:
                    x = self.EndX - self.nodesize
                if y + self.nodesize > self.EndY:
                    y = self.EndY - self.nodesize
                for yy in range(y, min(y + node_size, self.startY + self.worksize)):
                    for xx in range(x, min(x + node_size, self.startX + self.worksize)):
                        colors_list.append(self.pixels_list[yy][xx])
                most_common_color = Counter(colors_list).most_common(1)[0][0]
                if node_size not in self.colors_dict:
                    self.colors_dict[node_size] = {}
                self.colors_dict[node_size][(x, y)] = most_common_color

    def key_pressed(self, event):
        if event.key == "UP":
            if self.nodesize < 250:
                self.nodesize += 1
                self.isdraw = True

        elif event.key == "DOWN":
            if self.nodesize > 9:
                self.nodesize -= 1
                self.isdraw = True
            elif self.nodesize == 9:
                self.nodesize -= 1
                self.image = load_image("works/work6/scream.png")

                self.graphic.image(
                    self.image,
                    1280 / 2 - self.worksize / 2,
                    720 / 2 - self.worksize / 2,
                )
