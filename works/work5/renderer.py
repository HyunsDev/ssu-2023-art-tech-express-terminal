from ..common import Renderer
from random import choice, randint
from p5 import Vector, create_graphics

width, height = 1280, 720


def dot_wrapper(self, other):
    result = self.x * other.x + self.y * other.y
    return float(result)


Vector.dot = dot_wrapper


class Line:
    def __init__(self, startx, starty, endx, endy):
        self.startP = Vector(startx, starty)
        self.endP = Vector(endx, endy)
        self.position = (self.startP + self.endP) / 2
        self.radius = 10

    def draw(self, graphic):
        graphic.stroke(0)
        graphic.stroke_weight(5)
        graphic.line(self.startP.x, self.startP.y, self.endP.x, self.endP.y)
        return graphic


class Ball:
    def __init__(self, x, y, radius):
        self.position = Vector(x, y)  # 위치
        self.velocity = Vector(0, 0)  # 속도
        self.mass = 1  # 질량
        self.acceleration = Vector(0, 0)  # 가속도
        self.radius = radius
        self.isdrag = True
        self.originposition = self.position.copy()
        self.isCollision = False
        self.movedistance = (self.position - self.originposition).magnitude

    def apply_force(self, force):
        self.acceleration += force

    def update(self, context):
        self.originposition = self.position.copy()

        self.velocity += self.acceleration

        max_speed = 50
        self.velocity.limit(max_speed)

        self.position += self.velocity

        self.movedistance = (self.position - self.originposition).magnitude

        for k in context.Lines_list:
            context.check_collision(self, k)

        self.acceleration *= 0

    def draw(self, graphic):
        graphic.fill(255, 0, 0)
        graphic.circle(self.position.x, self.position.y, self.radius)

        graphic.circle(0, 0, 50)

        return graphic


class Work5Renderer(Renderer):
    def setup(self):
        self.Lines_list = []
        self.mainBall = None

        self.targetobj = None
        self.gravity = Vector(0, 1)
        self.clickposition = Vector(0, 0)
        self.roadDirection = Vector(1280, 720).normalize()
        self.originDirectoin = Vector(1280, 720).normalize()
        self.center = Vector(0, 0)
        self.saveDistance = 0
        self.updateDistance = 0
        self.restitution = 0.8
        self.closest_point = None

        self.graphic = create_graphics(width, height)

        self.mainBall = Ball(0, -100, 50)
        self.Lines_list.append(Line(-100, -100, 1280, 720))

    def draw(self):
        self.graphic = create_graphics(width, height)

        self.graphic.background(255)
        self.graphic.stroke(0)
        self.graphic.stroke_weight(3)

        self.mainBall.apply_force(self.gravity * self.mainBall.mass)  # F = ma
        self.mainBall.update(self)

        if self.roadDirection.x <= 0:
            self.updateDistance = 0
            self.saveDistance += self.mainBall.movedistance
        else:
            self.updateDistance = self.saveDistance
            self.saveDistance = 0
        PreviousLine = self.Lines_list[len(self.Lines_list) - 1].endP

        A = Line(
            PreviousLine.x,
            PreviousLine.y,
            PreviousLine.x
            + (self.mainBall.movedistance + self.updateDistance * 2)
            * self.roadDirection.x,
            PreviousLine.y
            + (self.mainBall.movedistance + self.updateDistance * 2)
            * self.roadDirection.y,
        )
        self.Lines_list.append(A)

        self.graphic.translate(
            width / 2 - self.mainBall.position.x, height / 2 - self.mainBall.position.y
        )
        self.graphic.stroke(0, 255, 0)
        self.center = Vector(self.mainBall.position.x, self.mainBall.position.y)

        self.graphic.stroke(0)

        self.graphic = self.mainBall.draw(self.graphic)
        for i in self.Lines_list:
            if (i.position - self.center).magnitude < 1000:
                self.graphic = i.draw(self.graphic)
            else:
                self.Lines_list.remove(i)

        return self.graphic

    def check_collision(self, ball, line):
        start_point = line.startP
        end_point = line.endP

        line_vector = end_point - start_point  # 선의 벡터값
        line_length = line_vector.magnitude  # 선의 길이값

        if line_length == 0:
            return

        line_direction = line_vector.normalize()  # 선의 방향벡터값

        line_to_ball = ball.position - start_point  # 공->시작점 벡터값
        line_to_ballOrigin = ball.originposition - start_point

        projection = line_to_ball.dot(line_direction)  # 선의 방향으로의 공의 투영 길이
        projectionOrigin = line_to_ballOrigin.dot(line_direction)

        projection = max(0, min(projection, line_length))  # 투영 길이를 선분 내에 유지
        projectionOrigin = max(0, min(projectionOrigin, line_length))

        self.closest_point = start_point + line_direction * float(
            projection
        )  # 선 위의 가장 가까운 점
        closest_pointOrigin = start_point + line_direction * float(projectionOrigin)

        distance_vector = ball.position - self.closest_point  # 공과 선 위의 가장 가까운 점의 벡터값
        distance_vectorOrigin = ball.originposition - closest_pointOrigin
        distance = distance_vector.magnitude  # 점과 선 사이의 거리

        if distance <= ball.radius / 2:
            ball.isCollision = True

            if (
                distance_vectorOrigin.y * distance_vector.y < 0
                and distance_vectorOrigin.x * distance_vector.x < 0
            ):  # 다음프레임때 선을 넘어가는경우
                ball.position = self.closest_point - distance_vector.normalize() * (
                    ball.radius / 2
                )
            else:
                ball.position = self.closest_point + distance_vector.normalize() * (
                    ball.radius / 2
                )

            velocity_projection = ball.velocity.dot(line_direction)
            ball.velocity = line_direction * velocity_projection

        else:
            ball.isCollision = False

    def mouse_dragged(self, event):
        mouseVector = Vector(
            event.x + self.center.x - width / 2, event.y + self.center.y - height / 2
        )

        self.roadDirection = (mouseVector - self.center).normalize()
        if self.roadDirection.x < 0:
            self.roadDirection = Vector(self.originDirectoin.x, self.originDirectoin.y)

    def mouse_released(self, event):
        self.roadDirection = Vector(1280, 720).normalize()
