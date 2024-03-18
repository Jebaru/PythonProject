# 👌
# # ##This code will not work in repl.it as there is no access to the colorgram package here.###
# # # #We talk about this in the video tutorials##
# # import colorgram
# #
# # rgb_colors = []
# # colors = colorgram.extract('image.jpg', 30)
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     rgb = (r, g, b)
# #     rgb_colors.append(rgb)
# #
# # print(rgb_colors)\
# #Mine
import random
from turtle import Turtle, Screen, colormode

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
drax = Turtle()
colormode(255)
drax.speed("fastest")
# pos = 0
#
# for i in range(10):
#     for j in range(10):
#         drax.pendown()
#         drax.dot(20, random.choice(color_list))
#         drax.penup()
#         drax.forward(50)
#         drax.pendown()
#     pos += 50
#     drax.penup()
#     drax.goto(0, pos)
#
# screen = Screen()
# screen.exitonclick()

# Video solution
drax.hideturtle()
drax.penup()
drax.setheading(225)
drax.forward(300)
drax.setheading(0)
no_of_dots = 100

for dots in range(1, no_of_dots+1):
    drax.dot(20, random.choice(color_list))
    drax.forward(50)

    if dots % 10 == 0:
        drax.setheading(90)
        drax.forward(50)
        drax.setheading(180)
        drax.forward(500)
        drax.setheading(0)

screen = Screen()
screen.exitonclick()