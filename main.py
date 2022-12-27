# import colorgram
#
# colors = colorgram.extract("image.jpg", 100)
#
# extracts = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     combo = (r, g, b)
#     extracts.append(combo)
#
# print(extracts)
#
# Upon printing out the color tuples in a list I commented
# out the extraction process as I don't need it anymore

import turtle as t
import random


palette = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
         (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
         (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174),
         (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63),
         (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")

timmy.hideturtle()
timmy.pu()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
lines = 100


for line in range(1, lines + 1):
    timmy.dot(20, random.choice(palette))
    timmy.forward(50)
    if line % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()

