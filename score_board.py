from turtle import Turtle

ALIGN = "center"
FONT = ("roboto", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.sety(260)
        self.color("white")
        self.show_score()

    def show_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)