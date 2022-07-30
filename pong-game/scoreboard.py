from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def score_left(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def score_right(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=0, y=260)
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)


