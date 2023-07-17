# From line 2 to 14, it is represented how we can extract the colors out of an image with the help of colorgram module
# import colorgram
#
# colors = colorgram.extract('20_001.jpg', 30)
#
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tupple = (r, g, b)
#     rgb_list.append(color_tupple)
#
# print(rgb_list)

import turtle
#Copy the rgb_list items in the color_list, and deletd the ones who have values which make white color
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()
