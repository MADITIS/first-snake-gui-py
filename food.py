import random
from turtle import Turtle

class Food(Turtle): #inheriting class Turtle (super class) to chile class (food)

    def __init__(self):
        super().__init__() #calling the super class and initializing it so child class can inherit attributes and methods from a super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= .5, stretch_wid= .5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        self.x_position = random.randint(-260,260)
        self.y_postiton = random.randint(-260,260)
        self.goto(self.x_position,self.y_postiton)    

        
