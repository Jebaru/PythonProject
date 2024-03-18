#👌
from turtle import Turtle, Screen
from random import randint
game_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
color = ["red", "pink", "yellow", "blue", "green", "purple"]
all_turtles = []
y_axis = -100

for i in range(6):
    baby_turtle = Turtle(shape="turtle")
    baby_turtle.color(color[i])
    baby_turtle.penup()
    baby_turtle.goto(x=-235, y=y_axis)
    y_axis += 40
    all_turtles.append(baby_turtle)

if bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            game_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've Won🥰! The {winner} turtle is the winner!")
            else:
                print(f"You've Lost🥲! The {winner} turtle is the winner!")
        dist = randint(0, 10)
        turtle.forward(dist)


screen.exitonclick()
