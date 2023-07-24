from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align='left', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align='center', font=FONT)
