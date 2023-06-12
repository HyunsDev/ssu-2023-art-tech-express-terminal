from ..common import Renderer
from random import choice, randint
from p5 import RIGHT, create_graphics, create_font, LEFT
import sys
import traceback
import re

shift_mapping = {
    "`": "~",
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
    "0": ")",
    "-": "_",
    "=": "+",
    "[": "{",
    "]": "}",
    "\\": "|",
    ";": ":",
    "'": '"',
    ",": "<",
    ".": ">",
    "/": "?",
}
pass_mapping = (
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
    "SHIFT",
    "META",
    "ALT",
    "CAPSLOCK",
    "CONTROL",
    "RIGHT",
    "LEFT",
)

indentation_spaces = 4


def get_indentation_spaces(line):
    indentation_count = 0
    for char in line.str:
        if char == " ":
            indentation_count += 1
        else:
            break
    return indentation_count


class Linestr:
    def __init__(self, str, x, y, graphic):
        self.str = str
        self.x = x
        self.y = y
        self.isActive = False
        self.error = False
        self.graphic = graphic

    def strdraw(
        self,
    ):
        if self.isActive:
            self.graphic.fill(255)
            self.graphic.stroke(0)
            self.graphic.rect(self.x, self.y, 1280, 15)
        self.graphic.fill(0)
        if self.error:
            self.graphic.fill(255, 0, 0)

        self.graphic.text(self.str, self.x, self.y)

        return self.graphic


class Work4Renderer(Renderer):
    def setup(self):
        self.isStart = True
        self.isActive = False
        self.TargetLine = None
        self.isShift = False
        self.Lines_list = []
        self.editing = True
        self.setuping = False
        self.FinalCode = ""
        self.draw_content = None

        self.graphic = create_graphics(1280, 720)

    def draw(self):
        if self.editing:
            self.graphic.background(255)  # 배경색을 흰색으로 변경
            self.graphic.no_stroke()
            self.graphic.fill(0)
            self.graphic.rect(0, 0, 100, 720)
            self.graphic.rect(0, 0, 1280, 100)
            self.graphic.fill(255)
            self.graphic.rect(100, 100, 1280, 10000)
            self.graphic.text_align(RIGHT)

            self.graphic.text_font(window.assets.getFont("D2Coding"))

            for i in range(41):
                self.graphic.text(str(i), 90, 100 + i * 15)
                self.Lines_list.append(Linestr("", 100, 100 + i * 15, self.graphic))

            self.isStart = False
            self.graphic.text_align(LEFT)

            self.graphic.fill(0)
            for i in self.Lines_list:
                self.graphic = i.strdraw()

        else:
            if self.setuping:
                self.graphic.background(255)
                exec(self.FinalCode)
                self.setuping = False

            try:

                def background(color):
                    self.graphic.background(color)

                def fill(color):
                    self.graphic.fill(color)

                def circle(x, y, radius):
                    self.graphic.circle(x, y, radius)

                def rect(x, y, width, height):
                    self.graphic.rect(x, y, width, height)

                def line(x1, y1, x2, y2):
                    self.graphic.line(x1, y1, x2, y2)

                def stroke(color):
                    self.graphic.stroke(color)

                fill(0)
                exec(self.draw_content)

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                line_number = traceback.extract_tb(exc_tb)[-1][1] - 1
                self.graphic.stroke(255, 0, 0)
                self.Lines_list[line_number].error = True

        return self.graphic

    def mouse_pressed(self, event):
        if self.editing:
            for i in self.Lines_list:
                i.isActive = False
            if 100 < event.x < 1200 and 100 < event.y:
                self.isActive = True
                self.TargetLine = self.Lines_list[(int(event.y) - 100) // 15]
                self.TargetLine.isActive = True

    def key_pressed(self, event):
        key = str(event.key)
        if self.editing:
            if key == "F5":
                self.FinalCode = ""
                for i in self.Lines_list:
                    i.error = False
                    self.FinalCode += i.str + "\n"

                match = re.search(
                    r"def draw\(\):\n(.*?)\n\n", self.FinalCode, re.DOTALL
                )
                if match:
                    self.draw_content = match.group(1)
                    indented_lines = []
                    for line in self.draw_content.split("\n"):
                        if line.startswith("    "):
                            indented_lines.append(line.strip())
                        else:
                            break
                    self.draw_content = "\n".join(indented_lines)
                    self.FinalCode = self.FinalCode.strip()
                    print(self.FinalCode)
                else:
                    print("draw 함수를 찾을 수 없습니다.")
                self.editing = False
                self.setuping = True

            if self.isActive:
                if key == "ENTER":
                    current_index = self.Lines_list.index(self.TargetLine)
                    next_index = current_index + 1
                    for i in range(next_index, len(self.Lines_list)):
                        self.Lines_list[i].y += 15
                    self.Lines_list.insert(
                        next_index,
                        Linestr("", 100, 100 + next_index * 15, self.graphic),
                    )
                    self.TargetLine = self.Lines_list[next_index]
                    if self.Lines_list[current_index].str.endswith(":"):
                        self.Lines_list[next_index].str += "    "
                    self.TargetLine.str += (
                        get_indentation_spaces(self.Lines_list[current_index]) * " "
                    )
                    for i in self.Lines_list:
                        i.isActive = False
                    self.TargetLine.isActive = True

                elif event.is_shift_down() and key in shift_mapping:
                    self.TargetLine.str += shift_mapping[key]

                elif key in pass_mapping:
                    pass
                elif key == "BACKSPACE":
                    if len(self.TargetLine.str) > 0:
                        self.TargetLine.str = self.TargetLine.str[:-1]

                        key = None
                    elif len(self.TargetLine.str) == 0:
                        current_index = self.Lines_list.index(self.TargetLine)
                        if current_index != 0:
                            self.TargetLine = self.Lines_list[current_index - 1]

                        for i in self.Lines_list:
                            i.isActive = False
                        self.TargetLine.isActive = True

                elif key == "SPACE":
                    self.TargetLine.str += " "
                    key = None
                elif key == "UP":
                    current_index = self.Lines_list.index(self.TargetLine)
                    if current_index != 0:
                        self.TargetLine = self.Lines_list[current_index - 1]

                    for i in self.Lines_list:
                        i.isActive = False
                    self.TargetLine.isActive = True

                elif key == "DOWN":
                    current_index = self.Lines_list.index(self.TargetLine)
                    if current_index != 0:
                        self.TargetLine = self.Lines_list[current_index + 1]

                    for i in self.Lines_list:
                        i.isActive = False
                    self.TargetLine.isActive = True
                elif key == "TAB":
                    self.TargetLine.str += indentation_spaces * " "
                else:
                    self.TargetLine.str += str(event.key)
        else:
            if key == "F4":
                self.setuping = False
                self.editing = True
                self.graphic.stroke_weight(1)
