from p5 import *

Lines_list = []
mainBall = None
width, height = 1280, 720
targetobj = None
gravity = Vector(0, 1)
clickposition = Vector(0, 0)
roadDirection = Vector(1280, 720).normalize()
originDirectoin = Vector(1280, 720).normalize()
center = Vector(0, 0)
saveDistance, updateDistance = 0, 0
restitution = 0.8
closest_point = None


def setup():
    global Lines_list, mainBall
    size(width, height)
    mainBall = Ball(0, -100, 50)
    Lines_list.append(Line(-100, -100, 1280, 720))


def draw():
    global mainBall, Lines_list, center, saveDistance, updateDistance

    background(255)
    strokeWeight(3)

    mainBall.apply_force(gravity * mainBall.mass)  # F = ma
    mainBall.update()

    if roadDirection.x <= 0:
        updateDistance = 0
        saveDistance += mainBall.movedistance
    else:
        updateDistance = saveDistance
        saveDistance = 0
    PreviousLine = Lines_list[len(Lines_list) - 1].endP

    A = Line(
        PreviousLine.x,
        PreviousLine.y,
        PreviousLine.x + (mainBall.movedistance + updateDistance * 2) * roadDirection.x,
        PreviousLine.y + (mainBall.movedistance + updateDistance * 2) * roadDirection.y,
    )
    Lines_list.append(A)

    translate(width / 2 - mainBall.position.x, height / 2 - mainBall.position.y)
    stroke(0, 255, 0)
    center = Vector(mainBall.position.x, mainBall.position.y)

    stroke(0)

    mainBall.display()
    for i in Lines_list:
        if (i.position - center).magnitude < 1000:
            i.display()
        else:
            Lines_list.remove(i)
        """
        if(i.endP.y <= center.y-height/2):
            Lines_list.remove(i)
        else:
            i.display()
        """


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

    def display(self):
        line(self.startP.x, self.startP.y, self.endP.x, self.endP.y)


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

    def update(self):
        self.originposition = self.position.copy()

        self.velocity += self.acceleration

        max_speed = 50
        self.velocity.limit(max_speed)

        self.position += self.velocity

        self.movedistance = (self.position - self.originposition).magnitude

        for k in Lines_list:
            check_collision(self, k)

        self.acceleration *= 0

    def display(self):
        fill(255, 0, 0)
        circle(self.position.x, self.position.y, self.radius)


def mouse_dragged(event):
    global roadDirection, mainBall, center

    mouseVector = Vector(
        event.x + center.x - width / 2, event.y + center.y - height / 2
    )

    roadDirection = (mouseVector - center).normalize()
    if roadDirection.x < 0:
        roadDirection = Vector(originDirectoin.x, originDirectoin.y)


def mouse_released(event):
    global roadDirection
    roadDirection = Vector(1280, 720).normalize()


def check_collision(ball, line):
    global closest_point
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

    closest_point = start_point + line_direction * float(projection)  # 선 위의 가장 가까운 점
    closest_pointOrigin = start_point + line_direction * float(projectionOrigin)

    distance_vector = ball.position - closest_point  # 공과 선 위의 가장 가까운 점의 벡터값
    distance_vectorOrigin = ball.originposition - closest_pointOrigin
    distance = distance_vector.magnitude  # 점과 선 사이의 거리

    if distance <= ball.radius / 2:
        ball.isCollision = True

        if (
            distance_vectorOrigin.y * distance_vector.y < 0
            and distance_vectorOrigin.x * distance_vector.x < 0
        ):  # 다음프레임때 선을 넘어가는경우
            ball.position = closest_point - distance_vector.normalize() * (
                ball.radius / 2
            )
        else:
            ball.position = closest_point + distance_vector.normalize() * (
                ball.radius / 2
            )

        velocity_projection = ball.velocity.dot(line_direction)
        ball.velocity = line_direction * velocity_projection

    else:
        ball.isCollision = False


run(sketch_preload=None, sketch_setup=setup, sketch_draw=draw, frame_rate=60)
