from turtle import Turtle
from random import choice  # Changed import

text = ["GAMEOVER", "MISSION FAILED", "THE HUNT IS OVER","DO BETTER","YOU TRIED"]

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.goto(x=0, y=270)
        self.color("white")
        self.game_over_text = choice(text)  # Fixed random selection
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.scores}", False, align="center", font=("Arial", 18, "normal"))
    
    def fail(self):
        self.goto(x=0, y=0)
        self.write(self.game_over_text, False, align="center", font=("Arial", 18, "normal"))  # Fixed variable name
    
    def addscore(self):
        self.scores += 1
        self.update()