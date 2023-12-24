import random
from turtle import Turtle, Screen


def drawLineAndTurn(turtle, sides):
    turtle.forward(100)
    turtle.right(360 / (sides))


def generateRandomNumber():
    return random.random()


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(0)
shape = 3

while shape <= 15:
    timmy_the_turtle.pencolor(generateRandomNumber(), generateRandomNumber(), generateRandomNumber())
    for i in range(shape):
        drawLineAndTurn(timmy_the_turtle, shape)
    shape += 1




screen = Screen()
screen.exitonclick()