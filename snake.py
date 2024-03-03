import turtle as t
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.segments = []  #segment creating for snake object
        self.create_snake() #it will run 
        self.head = self.segments[0]
  
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self,position):
        snake = t.Turtle(shape="square")
        snake.penup()
        snake.fillcolor("white")
        snake.goto(position)
        self.segments.append(snake)

    def clear_seg(self):
        for seg in self.segments:
            seg.goto(1500,1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
      

    def move(self):
        screen = t.Screen()  
        for seg in range(len(self.segments) - 1 , 0, -1):
            self.segments[seg].goto(self.segments[seg-1].pos())   
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    

    
                    