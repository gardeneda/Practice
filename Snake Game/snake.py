from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):  # This makes sense, because it wouldn't make the code readable if I just put it in
        for position in self.STARTING_POSITION:
            self.attach_tail(position)

    def attach_tail(self, position):
        # Add a new snake_body to the snake.
        new_turtle = Turtle(shape="square")
        new_turtle.pu()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.snake_body.append(new_turtle)

    def extend_tail(self):
        self.attach_tail(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):  # setheading here doesn't make sense here, because you're trying to "set" something whilst evaluating
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
