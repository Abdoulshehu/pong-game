# import colorgram
# colors = []
# color = colorgram.extract('image.jpg', 30)
# for i in range(0, 30):
#     first_color = color[i]
#     red = first_color.rgb
#     r = red.r
#     g = red.g
#     b = red.b
#     tupel = (r, g, b)
#     colors.append(tupel)
# print(colors)
colors = [(202, 164, 110),  (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 18 ), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
 (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
 (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as t
import random
t.colormode(255)
my_turtle = t
# my_turtle.setheading(225)
# my_turtle.forward(300)
# my_turtle.setheading(0)
no_of_dot = 100
num = 0
for i in range(1, no_of_dot):
    my_turtle.dot(20, random.choice(colors))
    my_turtle.forward(50)


    num += 10
    my_turtle.forward(num)
    my_turtle.setheading(90)
    my_turtle.forward(num)

    my_turtle.setheading(180)
    my_turtle.forward(num)

    my_turtle.setheading(270)
    my_turtle.forward(num)

    my_turtle.setheading(0)


my_screen =t.Screen()
my_screen.exitonclick()

