from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Move distance of each car in each refresh
MOVE_INCREMENT = 10  # Move distance increase every level up


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.level_completed = 0
        self.generation_possibility = 95
        self.car_list = []
        
        self.pu()
        self.hideturtle()

    def move_forward(self):
        for cars in self.car_list:
            distance_increase_by_level_completed = self.level_completed * MOVE_INCREMENT
            cars.forward(STARTING_MOVE_DISTANCE + distance_increase_by_level_completed)

    def create_car(self):
        new_turtle = Turtle("square")
        new_turtle.shapesize(stretch_wid=1, stretch_len=2)
        new_turtle.color(random.choice(COLORS))
        new_turtle.pu()
        new_turtle.goto(300, random.randint(-200, 300))
        new_turtle.setheading(180)
        self.car_list.append(new_turtle)

    def generate_block_of_cars(self):
        generation = self.generation_possibility - (self.level_completed * 15)
        for _ in range(random.randint(1, 100)):
            if generation < 0:
                if random.randint(0, 2) == 1:
                    self.create_car()
            if _ == generation:
                self.create_car()

    def delete_cars(self):
        for car in self.car_list:
            if car.xcor() < -320:
                car.hideturtle()
                del self.car_list[0]

    def reset_cars(self):
        for car in self.car_list:
            car.hideturtle()
        del self.car_list[:]

    def level_up(self):
        self.level_completed += 1
