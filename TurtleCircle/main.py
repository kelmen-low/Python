from turtle import Turtle, Screen
import random as r


def randomRGB():
    return r.random(),r.random(),r.random()


t = Turtle()

t.shape("circle")
t.speed(0)
t.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=0.3)
t.pensize(2)

for i in range(90):
    t.circle(200)
    t.right(4)



screen = Screen()
screen.exitonclick()
