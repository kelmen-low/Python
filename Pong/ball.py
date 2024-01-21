from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(0.5)
        self.reset()

    def move(self):
        self.forward(5)

    def bounce_x(self):
        current_heading = self.heading()
        print(current_heading)
        self.setheading(180 - current_heading)

    def bounce_y(self):
        current_heading = self.heading()
        self.setheading(360 - current_heading)

    def reset(self):
        self.hideturtle()
        self.setposition(0, 0)
        self.setheading(random.randint(115, 155))
        self.showturtle()