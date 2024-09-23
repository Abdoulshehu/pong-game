from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(width= 500, height= 400)
user_color = screen.textinput(title='turtle selector',  prompt="Select Your Turtle Color? ")
finish_line_turtle = Turtle()
finish_line_turtle.penup()
finish_line_turtle.goto(x=230, y= -190  ) 
finish_line_turtle.setheading(90)
finish_line_turtle.pendown()
finish_line_turtle.pensize(10)
finish_line_turtle.fd(400)
is_on = False
all_turtle = [] 
coordinates = [-70, -30, 10, 50, 90, 130]
color = ['red', 'blue', 'yellow', 'green', 'purple','orange']
for i in range(0, 6):
    blue_turtle = Turtle(shape='turtle')
    blue_turtle.penup()
    blue_turtle.goto(x=-230, y=coordinates[i])
    blue_turtle.color(color[i])
    all_turtle.append(blue_turtle)



if user_color:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_color:
                print(f"You've Won! The {winner_color} turtle wins!")
            else:
                print(f"You've Lose! The {winner_color} turtle wins!")
        distance =  random.randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()