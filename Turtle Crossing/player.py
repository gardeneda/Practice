from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() == 280:
            self.goto(STARTING_POSITION)
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

    def skip_to_next_level(self):
        self.forward(580)
