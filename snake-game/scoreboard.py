from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 16, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score = {str(self.score)}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!\n", align=ALIGN, font=GAME_OVER_FONT)
        self.write(f"Final Score = {self.score}", align=ALIGN, font=GAME_OVER_FONT)
