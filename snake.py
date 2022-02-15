from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.snake_head = self.turtles[0]

    def create_snake(self):
        for i in range(0, 3):
            snake_body = Turtle()
            snake_body.color("white")
            snake_body.shapesize(1)
            snake_body.shape("square")
            snake_body.penup()
            self.turtles.append(snake_body)

    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        self.snake_head.setheading(0)