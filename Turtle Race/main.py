from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your best', prompt='Which turtle do you think will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# jim = Turtle(shape="turtle")
# kim = Turtle(shape="turtle")
# lim = Turtle(shape="turtle")
# rim = Turtle(shape="turtle")
# dim = Turtle(shape="turtle")
#
# turtle_list = [tim, jim, kim, lim, rim, dim]
#
#
# y = -75
# for turtles in turtle_list:
#     turtles.pu()
#     turtles.goto(x=-230, y=y)
#     y += 35
#     turtles.color(colors.pop())

if user_bet:
    is_race_on = True

all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The winner of this race is the {winning_color} turtle!")
            is_race_on = False

screen.exitonclick()
