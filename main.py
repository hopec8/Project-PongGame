import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = t.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()


screen.update()

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_on = True
ball_move = True

while ball_move:
    screen.update()
    ball.move()

    if ball.xcor() > 395:
        ball.ball_reset()
        scoreboard.increase_score2()

    if ball.xcor() < -395:
        ball.ball_reset()
        scoreboard.increase_score1()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.distance(paddle_1) < 25 and ball.xcor() > 340:
        ball.bounce_paddle()

    if ball.distance(paddle_2) < 25 and ball.xcor() < -340:
        ball.bounce_paddle()

screen.exitonclick()