from turtle import *
from random import choice  # Import only what you need

# Setup the turtle
Joh = Turtle()
Tom = Turtle()
Joh.shape("turtle") 
# Define color and direction options
colours = ['blue', 'red', 'cyan', 'green','purple']  # Fixed: Removed duplicate 'blue'

for _ in range(200):
    Joh.color(choice(colours))  # Random color
    Joh.circle(60)
    Joh.right(30)
    Joh.speed('fastest')
    Tom.forward(60)
    Tom.right(45)
    Tom.forward(60)
    Tom.color(choice(colours))



screen = Screen()
screen.exitonclick()