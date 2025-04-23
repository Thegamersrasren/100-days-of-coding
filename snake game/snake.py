from turtle import Turtle

Startingposi = [(0,0), (-20,0), (-40,0)]
movedis = 20
Up = 90
down = 270
left = 180
right = 360
class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
    
    def createsnake(self):
        for posi in Startingposi:
           self.addsnake(posi)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(movedis)  # Fixed: changed self.head.segments[0] to self.head
    
    def up(self):
        if self.head.setheading != down:
            self.head.setheading(Up)  # Fixed: changed setheadings to setheading
    
    def down(self):
        if self.head.setheading != Up:
            self.head.setheading(down)  # Fixed: changed setheadings to setheading
    
    def left(self):
        if self.head.setheading != right:
            self.head.setheading(left)  # Fixed: changed setheadings to setheading
    
    def right(self):
        if self.head.setheading != left:
            self.head.setheading(right)  
    def addsnake(self, posi):
        Tim = Turtle()
        Tim.color("white")
        Tim.shape("square")
        Tim.penup()
        Tim.goto(posi)
        self.segments.append(Tim)
    def extend(self):
        self.addsnake(self.segments[-1].position())