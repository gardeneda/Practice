from turtle import Turtle


class Ball(Turtle):

    speed_ball = 1

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_x = 10
        self.ball_y = 10

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        self.speed(self.speed_ball)
        # self.left(36.869)

    def move(self):
        new_x = self.xcor() + self.ball_x
        new_y = self.ycor() + self.ball_y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.ball_y *= -1

    def bounce_paddle(self):
        self.ball_x *= -1

    def reset_ball(self, direction):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.ball_x = direction
        self.speed_ball = 1
        self.speed(self.speed_ball)

    def speed_up(self):
        self.speed_ball += 0.1
        self.speed(self.speed_ball)
