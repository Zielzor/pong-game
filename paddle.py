from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, loc):
        """" loc -> should be a tuple with x,y position"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(loc)

    def go_up(self):
        new_y = self.ycor()
        self.goto(x=self.xcor(), y=new_y + 15)

    def go_down(self):
        new_y = self.ycor()
        self.goto(x=self.xcor(), y=new_y - 15)
