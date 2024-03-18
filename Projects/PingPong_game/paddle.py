from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        cur_y = self.ycor() + 20
        self.goto(self.xcor(), cur_y)

    def go_down(self):
        curr_y = self.ycor() - 20
        self.goto(self.xcor(), curr_y)
