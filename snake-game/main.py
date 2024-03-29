from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundary import Boundary
import time


# Create the screen object with:
# Screen size, color and title
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake")

# Set the screen update tracer
screen.tracer(0)

# generate the Snake game objects onto the screen
snake = Snake()
food = Food()
scoreboard = Scoreboard()
boundary = Boundary()

# add key commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# turn on the game
game_is_on = True

# while the game is going, move the snake forward
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.add_point()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
