from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-280, 250)
        self.stage_level = 1
        self.print_stage()

    def print_stage(self):
        self.write(f"Level: {self.stage_level}", align="left", font=FONT)

    def stage_up(self):
        self.stage_level += 1
        self.clear()
        self.write(f"Level: {self.stage_level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
