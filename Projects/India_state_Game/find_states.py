import turtle
from tkinter import PhotoImage
import pandas


screen = turtle.Screen()
screen.title("Find States - India")
screen.bgcolor("#B163A3")
image = PhotoImage(file="india.gif").subsample(1, 2)
turtle.screensize(1250, 1250)
screen.addshape("image", turtle.Shape("image", image))
turtle.shape("image")

all_states_data = pandas.read_csv("india_states.csv")
all_states = all_states_data.state.to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) <= len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)}",
                                    prompt="Guess the states & Union Territories\nType \"Exit\" to learn unanswered "
                                           "states").title()
    if answer_state == "Exit":
        learn_missed_states = []
        for place in all_states:
            if place not in guessed_states:
                learn_missed_states.append(place)
        learn_df = pandas.DataFrame(learn_missed_states)
        learn_df.to_csv("learn_India_states.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = all_states_data[all_states_data.state == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(state_data["x"]), int(state_data["y"]))
        state_turtle.write(answer_state)
# screen.exitonclick()

