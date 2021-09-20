# import colorgram
import random
from turtle import Turtle, Screen, colormode


# def color_extractor(wanted_num_colors):
#     color_palette = []
#     colors = colorgram.extract('image.jpg', wanted_num_colors)
#     for objects in colors:
#         r = objects.rgb.r
#         g = objects.rgb.g
#         b = objects.rgb.b
#         new_rgb_tuple = r, g, b
#         color_palette.append(new_rgb_tuple)
#     return color_palette

# TODO: Paint a painting with 10 by 10 rows of spots.
# TODO: Each dot should be around 20 in size and spaced apart 50 paces.


def paint_row(turtle, list_containing_colors, num_circles):
    for _ in range(num_circles):
        turtle.dot(20, (random.choice(list_containing_colors)))
        turtle.fd(50)


# How do I change the position of the turtle to start printing from a different row at the most left-side?
# Use turtle.setpos(x, y)


color_palette = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

isaiah = Turtle()
colormode(255)
isaiah.speed(11)
isaiah.pu()
y = -150

for _ in range(10):
    isaiah.setpos(-250, y)
    paint_row(isaiah, color_palette, 10)
    y += 50

isaiah.hideturtle()
screen = Screen()
screen.screensize(1500, 1500)
screen.exitonclick()
