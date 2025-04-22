from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slithering Snake Game") 
screen.tracer(0)

Startingposi = [(0,0), (-20,0), (-40,0)]
segs = []

for posi in Startingposi:
    Tim = Turtle()
    Tim.color("white")
    Tim.shape("square")
    Tim.penup()
    Tim.goto(posi)
    segs.append(Tim)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segments in range(len(segs) - 1, 0, -1):
        x = segs[segments - 1].xcor()
        y = segs[segments - 1].ycor()
        Tom = segs[segments]
        Tom.goto(x, y)
    Tom[0].forward(40)
    Tom[0].left(90)





screen.exitonclick()