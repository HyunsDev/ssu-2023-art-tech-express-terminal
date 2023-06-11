from ..common import Renderer
from random import choice, randint
from p5 import create_graphics, radians, load_image, Vector, save_frame


class Work3Renderer(Renderer):
    def setup(self):
        self.button_images = []
        self.active_buttons = []

        self.smile_img = []
        self.light_img = []
        self.circle_image = []
        self.circle_choice_img = ""

        self.save_deactive_images = None
        self.save_button = "deactive"

        self.error_images = None

        self.frame = True
        self.smile_active = False

        self.draw_line = False
        self.path = []

        self.graphic = create_graphics(1280, 720)
        self.graphic.no_stroke()
        self.load_button_images()

    def draw(self):
        if self.frame:
            self.graphic.background(255)
            self.frame = False

        self.graphic.fill("#E6E6E6")
        self.graphic.no_stroke()
        self.graphic.rect_mode("CORNER")
        self.graphic.rect(0, 613, 1280, 108)

        if 0 in self.active_buttons:
            light_choice_img = choice(self.light_img)
            self.graphic.image(
                light_choice_img,
                randint(0, 1280) - 100,
                randint(0, 300) - 100,
            )

        # btn3이 활성화 되었을 경우
        if 2 in self.active_buttons:
            self.graphic.fill(255)
            self.graphic.circle(1280 / 2, 613 / 2, 500)

            self.graphic.push_matrix()
            self.graphic.translate(1280 / 2, 613 / 2)  # 캔버스의 중심점을 회전의 중심점으로 설정합니다
            self.graphic.rotate(radians(mouse_x))  # 마우스의 x좌표에 따라 red 이미지를 회전시킵니다.

            self.graphic.image(
                self.circle_image[0],
                -self.circle_image[0].width() / 2,
                -self.circle_image[0].height() / 2,
            )
            self.graphic.pop_matrix()

            self.graphic.push_matrix()
            self.graphic.translate(1280 / 2, 613 / 2)  # 캔버스의 중심점을 회전의 중심점으로 설정합니다
            self.graphic.rotate(radians(mouse_y))  # 마우스의 y좌표에 따라 blue 이미지를 회전시킵니다.
            self.graphic.image(
                self.circle_image[1],
                -self.circle_image[1].width() / 2,
                -self.circle_image[1].height() / 2,
            )
            self.graphic.pop_matrix()

        # 에러 버튼
        if 4 in self.active_buttons:
            self.graphic.image(self.error_images, 0, 0)
            self.active_buttons.remove(4)

        # 지우개 버튼
        if 5 in self.active_buttons:
            self.frame = True
            self.active_buttons.remove(5)

        self.draw_button()

        # 라인 그리기
        if self.draw_line and len(self.path) > 1:
            self.graphic.stroke(0)
            self.graphic.stroke_weight(5)
            for i in range(len(self.path) - 1):
                try:
                    self.graphic.line(
                        self.path[i].x,
                        self.path[i].y,
                        self.path[i + 1].x,
                        self.path[i + 1].y,
                    )
                except ZeroDivisionError:
                    # 0으로 나누기 예외 처리 코드 작성
                    print(
                        "ZeroDivisionError occurred. Please make sure the width and height are non-zero."
                    )

        return self.graphic

    def draw_button(self):
        # 일반 버튼 status
        for i in range(len(self.button_images)):
            if i in self.active_buttons:
                active_image = load_image(f"works/work3/source/btn/btn{i+1}-active.png")
                self.graphic.image(active_image, 355 + (i * 99), 627)
            else:
                self.graphic.image(self.button_images[i], 355 + (i * 99), 627)

        # save 버튼 status
        if self.save_button == "deactive":
            self.graphic.image(self.save_deactive_images, 1175, 628)
        else:
            save_active_image = load_image("works/work3/source/btn/save-active.png")
            self.graphic.image(save_active_image, 1175, 628)

    def load_button_images(self):
        self.save_deactive_images = load_image(
            "works/work3/source/btn/save-deactive.png"
        )

        # btn1 - red image
        for i in range(4):
            self.light_img.append(
                load_image(
                    f"works/work3/source/btn1_light/light-red-{100 + (i*50)}.png"
                )
            )
            self.light_img.append(
                load_image(
                    f"works/work3/source/btn1_light/light-yellow-{100 + (i*50)}.png"
                )
            )
            self.light_img.append(
                load_image(
                    f"works/work3/source/btn1_light/light-blue-{100 + (i*50)}.png"
                )
            )

        # btn2 - smile image
        for i in range(3):
            self.smile_img.append(
                load_image(f"works/work3/source/btn2_smile/smile-r-{50*(i+2)}.png")
            )
            self.smile_img.append(
                load_image(f"works/work3/source/btn2_smile/smile-y-{50*(i+2)}.png")
            )

        for i in range(6):
            button_image = load_image(f"works/work3/source/btn/btn{i+1}-deactive.png")
            self.button_images.append(button_image)

        # btn3 - circle
        for i in ["blue", "red", "yellow"]:
            self.circle_image.append(
                load_image(f"works/work3/source/btn3_circle/circle-{i}.png")
            )

        self.error_images = load_image("works/work3/source/btn5_error/error.png")

    def mouse_pressed(self, event):
        # 일반 버튼들 상태 전환
        for i in range(len(self.button_images)):
            button_x = 355 + (i * 99)
            button_y = 613
            button_width = 75
            button_height = 75

            if (
                button_x <= mouse_x <= button_x + button_width
                and button_y <= mouse_y <= button_y + button_height
            ):
                if i in self.active_buttons:
                    self.active_buttons.remove(i)
                    if i == 1:
                        self.smile_active = False
                else:
                    self.active_buttons.append(i)

        save_btn_x = 1175
        save_btn_y = 628

        # save 버튼 상태 전환
        if (
            save_btn_x <= mouse_x <= save_btn_x + button_width
            and save_btn_y <= mouse_y <= save_btn_y + button_height
        ):
            if self.save_button == "deactive":
                self.save_button = "active"
                # self.save_frame("output.png")  # 현재 프레임을 "output.png"로 저장
                self.save_button = "deactive"
            else:
                self.save_button = "deactive"

        # 스마일 버튼 생성
        if 1 in self.active_buttons:
            if self.smile_active:
                mousey = min(600, mouse_y)  # 마우스의 y 좌표가 613 이상이면 613으로 고정

                choice_smile_img = choice(
                    self.smile_img
                )  # 50에서 200 사이의 랜덤 크기 스마일 이미지 선택

                self.graphic.push_matrix()  # 현재 변환행렬 저장

                self.graphic.translate(mouse_x, mousey)  # 이미지를 그릴 위치로 이동
                self.graphic.rotate(radians(randint(-70, 70)))  # 랜덤한 각도로 회전
                self.graphic.image(
                    choice_smile_img,
                    -choice_smile_img.width() / 2,
                    -choice_smile_img.height() / 2,
                )  # 이미지의 중심이 (0, 0)에 위치하도록 이미지 그리기

                self.graphic.pop_matrix()  # 이전 변환행렬 복원
            else:
                self.smile_active = True

        # 라인 그리기 시작
        if 3 in self.active_buttons:
            self.draw_line = True
            self.path.append(Vector(mouse_x, mouse_y))

    def mouse_released(self, event):
        if 3 in self.active_buttons:
            self.draw_line = False
            self.path = []

    def mouse_dragged(self, event):
        if 3 in self.active_buttons:
            if self.draw_line:
                self.path.append(Vector(mouse_x, mouse_y))
