from p5 import *
import sys
import traceback
import re

isStart = True
isActive = False
TargetLine = None
isShift = False
Lines_list = []
editing = True
setuping = False
FinalCode = ""
draw_content = None

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


def setup():
    size(1280, 720)


def ddraw():
    if editing:
        global isStart, Lines_list, setuping
        background(255)  # 배경색을 흰색으로 변경
        no_stroke()
        fill(0)
        rect(0, 0, 100, 720)
        rect(0, 0, 1280, 100)
        fill(255)
        rect(100, 100, 1280, 10000)
        text_align(RIGHT)

        font = create_font("D2Coding.ttf", 15)
        text_font(font)

        for i in range(41):
            text(str(i), 90, 100 + i * 15)
            Lines_list.append(Linestr("", 100, 100 + i * 15))

        isStart = False
        text_align(LEFT)

        fill(0)
        for i in Lines_list:
            i.strdraw()
    else:
        if setuping:
            background(255)
            exec(FinalCode)
            setuping = False

        try:
            exec(draw_content)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            line_number = traceback.extract_tb(exc_tb)[-1][1] - 1
            stroke(255, 0, 0)
            Lines_list[line_number].error = True


def get_indentation_spaces(line):
    indentation_count = 0
    for char in line.str:
        if char == " ":
            indentation_count += 1
        else:
            break
    return indentation_count


class Linestr:
    def __init__(self, str, x, y):
        self.str = str
        self.x = x
        self.y = y
        self.isActive = False
        self.error = False

    def strdraw(self):
        if self.isActive:
            fill(255)
            stroke(0)
            rect(self.x, self.y, 1280, 15)
        fill(0)
        if self.error:
            fill(255, 0, 0)

        text(self.str, self.x, self.y)


def mouse_pressed(event):
    global isActive, TargetLine
    if editing:
        for i in Lines_list:
            i.isActive = False
        if 100 < event.x < 1200 and 100 < event.y:
            isActive = True
            TargetLine = Lines_list[(int(event.y) - 100) // 15]
            TargetLine.isActive = True


def key_pressed(event):
    global TargetLine, FinalCode, Lines_list, editing, setuping, draw_content
    key = str(event.key)
    if editing:
        if key == "F5":
            FinalCode = ""
            for i in Lines_list:
                i.error = False
                FinalCode += i.str + "\n"

            match = re.search(r"def draw\(\):\n(.*?)\n\n", FinalCode, re.DOTALL)
            if match:
                draw_content = match.group(1)
                indented_lines = []
                for line in draw_content.split("\n"):
                    if line.startswith("    "):
                        indented_lines.append(line.strip())
                    else:
                        break
                draw_content = "\n".join(indented_lines)
                FinalCode = FinalCode.strip()
            else:
                print("draw 함수를 찾을 수 없습니다.")
            editing = False
            setuping = True

        if isActive:
            if key == "ENTER":
                current_index = Lines_list.index(TargetLine)
                next_index = current_index + 1
                for i in range(next_index, len(Lines_list)):
                    Lines_list[i].y += 15
                Lines_list.insert(next_index, Linestr("", 100, 100 + next_index * 15))
                TargetLine = Lines_list[next_index]
                if Lines_list[current_index].str.endswith(":"):
                    Lines_list[next_index].str += "    "
                TargetLine.str += (
                    get_indentation_spaces(Lines_list[current_index]) * " "
                )
                for i in Lines_list:
                    i.isActive = False
                TargetLine.isActive = True

            elif event.is_shift_down() and key in shift_mapping:
                TargetLine.str += shift_mapping[key]

            elif key in pass_mapping:
                pass
            elif key == "BACKSPACE":
                if len(TargetLine.str) > 0:
                    TargetLine.str = TargetLine.str[:-1]

                    key = None
                elif len(TargetLine.str) == 0:
                    current_index = Lines_list.index(TargetLine)
                    if current_index != 0:
                        TargetLine = Lines_list[current_index - 1]

                    for i in Lines_list:
                        i.isActive = False
                    TargetLine.isActive = True

            elif key == "SPACE":
                TargetLine.str += " "
                key = None
            elif key == "UP":
                current_index = Lines_list.index(TargetLine)
                if current_index != 0:
                    TargetLine = Lines_list[current_index - 1]

                for i in Lines_list:
                    i.isActive = False
                TargetLine.isActive = True

            elif key == "DOWN":
                current_index = Lines_list.index(TargetLine)
                if current_index != 0:
                    TargetLine = Lines_list[current_index + 1]

                for i in Lines_list:
                    i.isActive = False
                TargetLine.isActive = True
            elif key == "TAB":
                TargetLine.str += indentation_spaces * " "
            else:
                TargetLine.str += str(event.key)
    else:
        if key == "F4":
            setuping = False
            editing = True
            stroke_weight(1)


run(sketch_draw=ddraw)
