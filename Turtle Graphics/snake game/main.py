from turtle import Screen
import time
from snake import Snake
from Food import food
from Score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slithering Snake Game") 
screen.tracer(0)


snakke = Snake()
foood = food()
score = Score()

screen.listen() 
screen.onkey(snakke.up, "Up")
screen.onkey(snakke.down, "Down")
screen.onkey(snakke.left, "Left")
screen.onkey(snakke.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakke.move()
    #detect food
    if snakke.head.distance(foood) < 15:
        foood.nextfood()
        score.addscore()
        snakke.extend()
        #detect wall
    if (snakke.head.xcor() > 280 or snakke.head.xcor() < -280 or 
        snakke.head.ycor() > 280 or snakke.head.ycor() < -280):
        score.resetscore
        snakke.reset
        
    for segment in snakke.segments[1:]:
        if snakke.head.distance(segment) < 10:
            score.resetscore()
screen.exitonclick()