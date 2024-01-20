from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-310, 310)
        self.hideturtle()
        self.pencolor("white")
        self.pendown()
        self.goto(310, 310)
        self.goto(310, -310)
        self.goto(-310, -310)
        self.goto(-310, 310)
        self.penup()
