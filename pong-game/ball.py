from turtle import Turtle

XPOS = 0
YPOS = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(XPOS, YPOS)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_bounce(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.x_move *= -1
        self.y_move *= -1
        # self.goto(self.x_move, self.y_move)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def ball_missed(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

