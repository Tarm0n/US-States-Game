import turtle
import pandas

screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.penup()
screen.title("U.S. States Game")
data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_list = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{len(guessed_states)}/50 States Correct").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    for state in state_list:

        if answer_state == state and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            states = data[data.state == answer_state]
            t.goto(states.x.iloc[0], states.y.iloc[0])
            t.write(answer_state)

