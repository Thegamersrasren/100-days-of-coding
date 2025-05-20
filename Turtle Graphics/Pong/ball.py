from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10  # Slower horizontal movement
        self.y_move = 10 # Slower vertical movement
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1
        # Removed speed increase to keep movement slow

    def bounds(self):
        self.goto(0, 0)
        self.x_move *= -1  # Change direction after reset