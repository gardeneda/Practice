from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


# Turtles are width=20, height=20

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)


# for _ in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.goto(init_position[_])
#     snake_body.append(new_turtle)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
print(scoreboard.high_score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food. (turtle.distance)
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_tail()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for _ in range(1, len(snake.snake_body) - 1):
        if snake.head.distance(snake.snake_body[_]) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
