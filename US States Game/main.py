import turtle
import pandas


def get_mouse_click_coor(x, y):
    print(x, y)


data = pandas.read_csv("./50_states.csv")
# print(data)
state_data = data["state"].to_list()
# print(state_data)

test_sample = (data[data.state == "Florida"])
# print(test_sample["x"][state_data.index("Florida")])


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle.listen()
turtle.onscreenclick(get_mouse_click_coor)


correct_guesses = []
writer = turtle.Turtle()
writer.hideturtle()

while len(correct_guesses) < 50:

    answer_state = (screen.textinput(title=f"({len(correct_guesses)}/50) States Correct",
                                     prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        break

    if answer_state in state_data and answer_state not in correct_guesses:

        target_state = (data[data.state == answer_state])
        target_x = (target_state["x"][state_data.index(answer_state)])
        target_y = (target_state["y"][state_data.index(answer_state)])

        writer.pu()
        writer.goto(x=target_x, y=target_y)
        writer.pd()
        writer.write(f"{answer_state}")

        correct_guesses.append(answer_state)

A = set(state_data)
B = set(correct_guesses)

states_to_guess = list(A - B)
print(states_to_guess)

missed_states_data = {
    "Missed Guesses": states_to_guess,
}

missed_states_df = pandas.DataFrame(missed_states_data)
missed_states_df.to_csv("to_learn_list.csv")
