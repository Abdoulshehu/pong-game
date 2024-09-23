from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__() 
        self.score = 0  
        self.hideturtle()  
        self.goto(x=0, y=260) 
        self.color("white")  
        self.write(f'Score:{self.score}', False, align='center', font=("Courier", 15, "normal"))

    def game_over(self):
             self.goto(0,0)
             self.write('GAME OVER!!', False, align='center', font=("Courier", 24, "normal"))
             
        
        
    def increase_score(self):
        self.clear()
        self.score += 1 
        self.write(f'Score:{self.score}', False, align='center', font=("Courier", 15, "normal"))

    def next_level(self):
         if self.score >= 4:
              return True       