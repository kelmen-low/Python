from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 16, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def add_point(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {str(self.score)} High Score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore(self.score)
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!\n", align=ALIGN, font=GAME_OVER_FONT)
        self.write(f"Final Score = {self.score}", align=ALIGN, font=GAME_OVER_FONT)

    def get_highscore(self):

        with open("data.txt") as file:
            highscore = file.read()
            print(highscore)
            return int(highscore)

    def set_highscore(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))
