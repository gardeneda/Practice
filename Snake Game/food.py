from turtle import Turtle
import random

SCREEN_RANGE_X = -280, 280
SCREEN_RANGE_Y = -280, 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # We use this here, because this method needs to be initiated at the beginning as well.

    def refresh(self):
        random_x = random.randint(SCREEN_RANGE_X[0], SCREEN_RANGE_X[1])
        random_y = random.randint(SCREEN_RANGE_Y[0], SCREEN_RANGE_Y[1])
        self.goto(random_x, random_y)
