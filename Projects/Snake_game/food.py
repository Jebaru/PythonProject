import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("purple")
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-270, 265)
        y_axis = random.randint(-270, 265)
        self.goto(x_axis, y_axis)
