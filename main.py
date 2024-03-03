import random
from tracemalloc import start
import turtle as t
import time
import snake
import food
import scoreboard

#make the canvas background black and make a snake with squares

screen = t.Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = snake.Snake() #this is creating the snake segment
food = food.Food()
scoreboard = scoreboard.ScoreBoard()
# starting_position = [(0, 0), (-20, 0), (-40,0)]
# segments = []
# for position in starting_position:
#     snake = t.Turtle(shape="square")
#     snake.penup()
#     snake.fillcolor("white")
#     snake.goto(position)
#     segments.append(snake)


snake.move()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(1)
#     for seg in range(2 , 0, -1):
#         segments[seg].goto(segments[seg-1].pos())   
#     segments[0].forward(20)

       
#move the snake


# screen.onkeyrelease(key="w", snake.move_forward)

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , key = "Down")
screen.onkey(snake.left , key = "Left")
screen.onkey(snake.right , key = "Right")
game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
                scoreboard.increase_score()
                snake.extend()
                food.refresh()


        elif snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                scoreboard.reset()
                snake.clear_seg()


        for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:

                        scoreboard.reset()
                        snake.clear_seg()
#control the snake


#randomize the food and interaction with it


#calculate the score and show on the canvas


#game over when the snake hits the wall or itself

screen.exitonclick()
