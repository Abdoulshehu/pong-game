from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time



screen = Screen()
screen.title("Snake Level 1")
screen.setup(width=600, height=600)
screen.bgcolor(0,0,0)
screen.tracer(0)


snake = Snake()
food = Food()


score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_growth()
        score_board.increase_score()
       
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.game_over()
        game_on = False
    
    for segment in snake.segments[1:]:
                
        if snake.head.distance(segment) < 10 :
            game_on = False
            score_board.game_over()
            
screen.exitonclick()





 