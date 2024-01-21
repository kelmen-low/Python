from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(0, 450)
        self.clear()
        self.write("SCORE", align=ALIGN, font=FONT)
        self.goto(0, 400)
        self.write(f"{self.score1}   {self.score2}", align=ALIGN, font=FONT)
