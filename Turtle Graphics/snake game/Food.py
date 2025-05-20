from turtle import Turtle
from random import randint

class food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape=("circle")
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.nextfood()
    def nextfood (self):
        randx = randint(-270,270)
        randy = randint(-270,270)
        self.goto(randx,randy)
        
        