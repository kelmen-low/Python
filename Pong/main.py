from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from midfield import Midfield
from ball import Ball
import time

LEFT_START_POSITION = -600
RIGHT_START_POSITION = 600

# Create the screen
screen = Screen()
scoreboard = Scoreboard()
midfield = Midfield()
ball = Ball()

# Set the screen settings
screen.bgcolor("black")
screen.screensize(1000, 1000)
screen.listen()
screen.tracer(0)

# Add the paddles and configure motions
paddle1 = Paddle(LEFT_START_POSITION)
paddle2 = Paddle(RIGHT_START_POSITION)

# Event listen for paddle 1 inputs
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

# Event listen for paddle 2 inputs
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

# Event listen for start game
screen.onkey(ball.move(), "Enter")

# Update the screen once objects are initialized
screen.update()

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # If the ball hits ceiling or floor
    if ball.ycor() <= -525 or ball.ycor() >= 525:
        ball.bounce_y()

    # If the ball hits a paddle
    if (-590 >= ball.xcor() >= -600 and paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50) or (
            590 <= ball.xcor() <= 600 and paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
        ball.bounce_x()

    # If the ball goes off left side
    if ball.xcor() < -650:
        scoreboard.score1 += 1
        scoreboard.update()
        ball.reset()

    # If the ball goes off right side
    if ball.xcor() > 650:
        scoreboard.score2 += 1
        scoreboard.update()
        ball.reset()


screen.exitonclick()