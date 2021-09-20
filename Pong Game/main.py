# TODO: Create a Screen
# TODO: Create a Paddle class (You're going to create two, and these two has to be used by different users
# The paddles will have to move, two different sets of input.
# Create the paddle
# Move the paddle to user command
# Check when paddle comes in contact with the ball
# TODO: Create a ball class (Remember that the ball has to be able to bounce off surfaces
# Create the ball, the ball moves at a constant rate of speed
# The ball needs to bounce of surfaces, maybe invert the angle?
# TODO: Create a separate class for 'scoreboard'

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    print(ball.speed_ball)
    ball.move()

    # Detect collision of the ball with the top and bottom wall.
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_wall()

    # Detect collision of the ball with the paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        ball.speed_up()

    # Detect if the paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_ball(10)  # If the right paddle misses the ball, the ball should go to the right
        left_paddle.reset_game(-350, 0)
        right_paddle.reset_game(350, 0)
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_ball(-10)
        left_paddle.reset_game(-350, 0)
        right_paddle.reset_game(350, 0)
        scoreboard.r_point()

screen.exitonclick()
