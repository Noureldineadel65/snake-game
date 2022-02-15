from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Python Snake Game")
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()