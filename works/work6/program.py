from collections import Counter
from p5 import *

nodes_list = [[]]
colors_dict = {}
nodesize = 8
width, height = 1280, 720
pixels_list = [[]]
start = True
isdraw = False
startX, startY = 390, 60
worksize = 500
EndX, EndY = startX + worksize, startY + worksize


def setup():
    global pixels_list
    noStroke()
    size(width, height)


def loadimage():
    global pixels_list
    pixels_list = [[0 for _ in range(height)] for _ in range(width)]
    load_pixels()
    for x in range(startX, EndX):
        for y in range(startY, EndY):
            index = (x, y)
            p = pixels[index]
            a = (int(p.red), int(p.green), int(p.blue))
            pixels_list[x][y] = a
    update_pixels()


def calculate(node_size):
    global colors_dict
    colors_dict = {}
    for x in range(startX, EndX, node_size):
        for y in range(startY, EndY, node_size):
            colors_list = []
            if x + nodesize > EndX:
                x = EndX - nodesize
            if y + nodesize > EndY:
                y = EndY - nodesize
            for yy in range(y, min(y + node_size, startY + worksize)):
                for xx in range(x, min(x + node_size, startX + worksize)):
                    colors_list.append(pixels_list[xx][yy])
            most_common_color = Counter(colors_list).most_common(1)[0][0]
            if node_size not in colors_dict:
                colors_dict[node_size] = {}
            colors_dict[node_size][(x, y)] = most_common_color


def draw():
    global nodes_list, isdraw, nodesize, start
    if start:
        background(255)
        image(loadImage("works/work6/scream.jpg"), startX, startY, worksize, worksize)
        loadimage()

        start = False

    if isdraw:
        fill(255)
        rect(startX, startY, worksize, worksize + 101)
        nodes_list = [[] for _ in range(width // nodesize)]
        calculate(nodesize)
        for x in range(startX, EndX, nodesize):
            for y in range(startY, EndY, nodesize):
                if x + nodesize > EndX:
                    x = EndX - nodesize
                if y + nodesize > EndY:
                    y = EndY - nodesize
                node_color = colors_dict[nodesize][(x, y)]
                nodes_list[x // nodesize].append(
                    node(x, y, node_color, nodesize, nodesize)
                )
                nodes_list[x // nodesize][-1].nodedraw()

        isdraw = False


class node:
    def __init__(self, left_topX, left_topY, avgcolor, Length, Height):
        self.x = left_topX
        self.y = left_topY
        self.avgcolor = avgcolor
        self.l = Length
        self.h = Height

    def nodedraw(self):
        fill(*self.avgcolor)
        rect(self.x, self.y, self.l, self.h)


def key_pressed(event):
    global nodes_list, nodesize, isdraw

    if event.key == "UP":
        if nodesize < 250:
            nodesize += 1
            isdraw = True

    elif event.key == "DOWN":
        if nodesize > 9:
            nodesize -= 1
            isdraw = True
        elif nodesize == 9:
            nodesize -= 1
            image(
                loadImage("works/work6/scream.jpg"), startX, startY, worksize, worksize
            )


run()
