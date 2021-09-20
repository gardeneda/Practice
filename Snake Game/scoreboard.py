from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.score_count = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score_count}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_count > self.high_score:
            with open("data.txt", mode='w') as highscore:
                highscore.write(f"{self.score_count}")
                self.high_score = self.score_count
        self.score_count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
