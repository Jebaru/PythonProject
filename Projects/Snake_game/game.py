# 👌
from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

ekans = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(ekans.up, "Up")
screen.onkey(ekans.down, "Down")
screen.onkey(ekans.left, "Left")
screen.onkey(ekans.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    ekans.move()

    # collision with food
    if ekans.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        ekans.extend()

    # Wall Collision
    if ekans.head.xcor() > 280 or ekans.head.xcor() < -300 or ekans.head.ycor() > 300 or ekans.head.ycor() < -300:
        # game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        ekans.reset()

    # Tail collision
    for seg in ekans.segments[1:]:
        if ekans.head.distance(seg) < 10:
            # game_on = False
            scoreboard.reset()
            ekans.reset()
            #scoreboard.game_over()

screen.exitonclick()
