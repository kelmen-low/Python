from turtle import Turtle


class Midfield(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.dotted_line()

    def dotted_line(self):
        self.goto(0, 1000)

        for i in range(60):
            self.pendown()
            current_y = self.ycor()
            self.sety(current_y - 20)
            self.penup()
            self.sety(current_y - 40)
