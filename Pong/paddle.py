from turtle import Turtle
MOVEMENT_DISTANCE = 40


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.speed(0)
        self.create_paddle()
        self.setx(start_position)
        self.sety(0)

    def create_paddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)

    def up(self):
        current_y = self.ycor()
        self.sety(current_y + MOVEMENT_DISTANCE)

    def down(self):
        current_y = self.ycor()
        self.sety(current_y - MOVEMENT_DISTANCE)