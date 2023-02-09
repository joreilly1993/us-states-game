from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title(f"U.S. States Game")

turtle = Turtle()
turtle.shape(image)

guessed_states = []
missed_states = []


should_continue = True
while should_continue:
    answer_state = screen.textinput(title=f"States Correct: {len(guessed_states)}/50", prompt="Name a state:").title()
    states_data = pandas.read_csv("50_states.csv")
    states_list = states_data["state"].to_list()
    user_guess = states_data[states_data.state == answer_state]

    if answer_state == "Exit":
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("missed_states.csv")
        break
    if answer_state in states_list and answer_state not in guessed_states:
        x = int(user_guess["x"])
        y = int(user_guess["y"])
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.write(answer_state)
        guessed_states.append(answer_state)

# states to learn csv



