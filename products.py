# import turtle as t
# import random
# t.colormode(255)
# my_turtle = t
# my_turtle.speed(0)
#
# def turtle_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# direction = [90, 0, 180, 270 ]
# for _ in range(100):
#      my_turtle.dot(2)
#      my_turtle.fd(100)


# t.exitonclick()
# t.title("Geometry")
colors = [(202, 164, 110),  (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 18 ), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
 (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
 (107, 127, 153), (176, 192, 208), (168, 99, 102)]


import turtle as t
import random
t.colormode(255)


my_turtle = t
my_turtle.speed(0)
my_turtle.penup()
my_turtle.hideturtle()


my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)


no_of_dot = 101
for i in range(1, no_of_dot):
    my_turtle.dot(20, random.choice(colors))
    my_turtle.forward(50)
    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


my_screen =t.Screen()
my_screen.exitonclick()





# def size_gap(size):
#      for i in range(int(360/size)):
#           my_turtle.circle(100)
#           current_heading = my_turtle.heading()
#           my_turtle.setheading(current_heading + size)
#           tup = turtle_color()
#           my_turtle.pencolor(tup)
# size_gap(5)    
# def draw_shape(num_of_side):
#     angle = 360/ num_of_side
#     for i in range(num_of_side):
#          my_turtle.forward(100)
#          my_turtle.right(angle)
# for i in range(3,11):
#      draw_shape(i)
#      my_turtle.color(random.choice(color))