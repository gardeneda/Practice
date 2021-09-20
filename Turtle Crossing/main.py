import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
user_turtle = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user_turtle.move_up, "Up")
screen.onkey(user_turtle.skip_to_next_level, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.generate_block_of_cars()
    manager.move_forward()
    manager.delete_cars()

    # Check collision of turtle and car
    for car in manager.car_list:
        if car.distance(user_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if turtle reaches the finish line
    if user_turtle.ycor() >= 280:
        user_turtle.reset_turtle()
        manager.level_up()
        print(manager.level_completed)
        manager.reset_cars()
        print(manager.car_list)
        scoreboard.stage_up()

screen.exitonclick()
