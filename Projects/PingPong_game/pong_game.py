# 👌
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# r_paddle = Paddle((375, 0))
# l_paddle = Paddle((-375, 0))
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

    # Detect Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect paddle and ball Collision:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # R-Paddle Misses
    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_point()

    # L-Paddle Misses:
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
