from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
    
    def refresh(self):
        ramdom_x = random.randint(-280, 280)
        ramdom_y = random.randint(-280, 280)
        self.goto(ramdom_x, ramdom_y)

