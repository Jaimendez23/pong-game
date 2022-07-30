from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()

        self.XPOS = xpos
        self.YPOS = ypos
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.XPOS, self.YPOS)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.XPOS, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.XPOS, new_y)





