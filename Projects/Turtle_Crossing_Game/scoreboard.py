from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_increase(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

