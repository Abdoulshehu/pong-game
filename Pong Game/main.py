from turtle import Screen
from paddle import Paddle, Ball, ScoreBoard
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Creating both right and left paddle
paddle_r = Paddle((480, 0))
paddle_l = Paddle((-480, 0))

# Creating a score_board board
score_board = ScoreBoard()


# Create a Ball
ball = Ball()


screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")


def reset_paddles():
     paddle_l.goto(-480, 0)
     paddle_r.goto(480, 0)

# Start Game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    
    ball.move_NE()
   
    if ball.ycor() > 370 or ball.ycor() < -370 :
        ball.bounce()


    if ball.xcor() > 480:
        score_board.game_over(('ONE'))
        screen.delay(100)
        ball.reset_ball()
        score_board.reset_score()
        reset_paddles()
        
       
   
   
   
    if ball.xcor() < -480:
        score_board.game_over(('TWO'))
        screen.delay(100)
        ball.reset_ball()
        score_board.reset_score()
        reset_paddles()
       
        
       
    if ball.distance(paddle_r) < 50 and ball.xcor() > 370:
        ball.collision()
        score_board.r_score()
       
    
    if ball.distance(paddle_l) < 50 and ball.xcor() < -370:
        ball.collision()
        score_board.l_score()
        
        

screen.exitonclick()