from turtle import Screen
from snake_file import Snake
import time
from food import Food
from scoreboard import Scoreboard

# Controlling the Screen
screen_of_game = Screen()
screen_of_game.screensize(canvwidth=600,canvheight=600,bg="black")
screen_of_game.title(titlestring="Welcome To SNAKE Game...")
screen_of_game.tracer(0)

# Controlling and create Snake
snake = Snake()
screen_of_game.listen()
screen_of_game.onkey(fun=snake.up,key="Up")
screen_of_game.onkey(fun=snake.down,key="Down")
screen_of_game.onkey(fun=snake.right,key="Right")
screen_of_game.onkey(fun=snake.left,key="Left")

#COntrol and Create food
food = Food()
score = 0

# SCore
score = Scoreboard()

# Run The snake
game_is_on = True
while game_is_on :
    screen_of_game.update()
    time.sleep(0.1)
    snake.move()
    
    # Collide with food
    if snake.square_segments[0].distance(food) < 15:
        food.refresh()
        score.is_increase()
        snake.extend_snake()
        
    #Detect collision with wall
    if snake.square_segments[0].xcor() >= 470 or snake.square_segments[0].xcor() <= -485 or snake.square_segments[0].ycor() >= 420 or snake.square_segments[0].ycor() <= -401 :
        print("Game Over")
        game_is_on = False
        score.game_over()
    
    # Detect with the collide with taile.
    # ANy segment collide with the head
    for each_segment in snake.square_segments[1:]:
        # if each_segment == snake.square_segments[0]:
        #     pass
        if snake.square_segments[0].distance(each_segment) < 10:
            print("Game Over")
            game_is_on = False
            score.game_over()
            
        
   



screen_of_game.exitonclick()