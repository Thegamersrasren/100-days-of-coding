from turtle import Turtle, Screen
Joh = Turtle()
screen = Screen()
def move ():
    Joh.forward(10)
def back():
    Joh.back(10)
def up():
    new_heading = Joh.heading() + 30
    Joh.setheading(new_heading)
def down ():
    new_heading = Joh.heading() - 30
    Joh.setheading(new_heading)
def clear():
    Joh.clear()
    Joh.home()
    Joh.penup()
    Joh.pendown()
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=up)
screen.onkey(key="d", fun=down)
screen.onkey(key="c", fun=clear)

screen.exitonclick()