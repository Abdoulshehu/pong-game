from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid= 7)
        self.goto(position)

    def move_up(self):
       new_y = self.ycor() + 30
       self.goto(self.xcor(), new_y)
   
    def move_down(self):
       new_y = self.ycor() - 30
       self.goto(self.xcor(), new_y)
    

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10  
        self.move_speed = 0.1

        
    def move_NE(self):    
       new_x = self.xcor() + self.x_move 
       new_y = self.ycor() + self.y_move
       self.goto(new_x, new_y)
    
    def bounce(self):
      self.y_move *= -1

    def collision(self):
       self.x_move *= -1
       self.move_speed *= 0.8
    
    def reset_ball(self):
        self.goto(0,0)  
        self.x_move *= -1
        self.move_speed = 0.1
       

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__() 
        self.r_point = 0  
        self.l_point = 0
        self.hideturtle()  
        self.color("white")   
        self.penup()    
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-200, 350)
        self.write(f'Player One:{self.l_point}', False, align='center', font=("Courier", 15, "normal"))
        self.goto(200, 350)
        self.write(f'Player Two:{self.r_point}', False, align='center', font=("Courier", 15, "normal"))
       

    def r_score(self):
         self.r_point += 1  
         self.update_score()

    def l_score(self):
         self.l_point += 1  
         self.update_score()

    def reset_score(self):
        self.l_point *= 0
        self.r_point *= 0 
    
    def game_over(self, player_win):
         self.goto(0,0)
         self.write(f'PLAYER {player_win} WINS', False, align='center', font=("Courier", 24, "normal"))
         self.reset_score()
        
