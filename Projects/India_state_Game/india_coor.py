import turtle
from tkinter import PhotoImage


def get_coor_on_click(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("Find States - India")
screen.bgcolor("#B163A3")
# image = "india.gif"
# screen.addshape(image)
# turtle.shape(image)
image = PhotoImage(file="india.gif").subsample(1, 2)
turtle.screensize(1250, 1250)
screen.addshape("image", turtle.Shape("image", image))
turtle.shape("image")
# turtle.resizemode("auto")
turtle.onscreenclick(get_coor_on_click)
turtle.mainloop()
