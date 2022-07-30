# screen, create and move paddle, create another paddle, create the ball and make it move
# detect collision with wall, detect collision with paddle, detect when paddle misses, keep score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

xpos1 = 350
ypos = 0
xpos2 = -350

r_paddle = Paddle(xpos1, ypos)
l_paddle = Paddle(xpos2, ypos)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_bounce()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.score_left()
        ball.ball_missed()

    if ball.xcor() < -380:
        score.score_right()
        ball.ball_missed()

screen.exitonclick()

