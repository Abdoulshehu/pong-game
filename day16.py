from turtle import Turtle, Screen
from prettytable import PrettyTable

# my_turtle = Turtle()
# my_turtle.shape("turtle")
# print(my_turtle)
# my_turtle.color("Red")
# my_turtle.forward(100)
#
#
#
#
#
# my_turtle.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column('Names', ['ADDULLAHI', 'SHEHU', 'USMAN',])
table.add_column('Age', [20, 30, 25])
table.align = "l"
print(table)


