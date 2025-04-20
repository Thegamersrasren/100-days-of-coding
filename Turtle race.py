from turtle import Turtle, Screen
from random import randint

screen = Screen()
is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Choose your turtle", 
                          prompt="Which turtle will win the race? (blue, red, pink, green, purple or orange)").lower()  # Added parentheses to lower()
print(user_bet)
y_positions = [-120, -70, -20, 30, 80, 130]
colours = ['blue', 'red', 'pink', 'green', 'purple', 'orange']
all_joh = []

for turtle_index in range(6):
    joh = Turtle(shape="turtle")
    joh.color(colours[turtle_index])
    joh.penup()
    joh.goto(x=-230, y=y_positions[turtle_index])
    all_joh.append(joh)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_joh:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        
        if turtle.xcor() > 230:  # Fixed xcor to xcor()
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"The winning turtle is {winner}. You win!")
            else:
                print(f"The winning turtle is {winner}. You lose!")
            break  # Exit the loop once we have a winner

screen.exitonclick()