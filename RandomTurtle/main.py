from turtle import Turtle, Screen
import random as r


def randomRGB():
    return r.random(),r.random(),r.random()


def randomDirection(turtle):
    return turtle.setheading(r.choice([0, 90, 180, 270]))


t = Turtle()

t.shape("circle")
t.speed(0)
t.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=0.3)
t.pensize(5)

for i in range(100):
    t.color(randomRGB())
    randomDirection(t)
    t.forward(20)



screen = Screen()
screen.exitonclick()
