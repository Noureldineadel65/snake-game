import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        turtle.color("white")
        turtle.hideturtle()
        turtle.penup()
        turtle.setposition(0 , 250)
        self.update_score()

    def update_score(self):
        turtle.clear()
        self.score += 1
        turtle.write(f"Score: {self.score}", align="center", font=('Courier', 20, 'italic'))