from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_x, start_y):
        super().__init__()
        self.create_paddle(start_x, start_y)

    def create_paddle(self, start_x, start_y):
        self.shape("square")
        self.color("white")
        self.pu()
        self.goto(start_x, start_y)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)

    def reset_game(self, x, y):
        self.goto(x, y)
