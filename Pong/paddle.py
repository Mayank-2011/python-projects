from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_down(self):
        self.sety(self.ycor()-20)

    def move_up(self):
        self.sety(self.ycor()+20)
