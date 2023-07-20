from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
