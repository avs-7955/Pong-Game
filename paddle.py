from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positionn):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(positionn)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)

    def move_up(self):
        '''Function to move the paddle upwards.'''
        self.forward(20)

    def move_down(self):
        '''Function to move the paddle downstairs.'''
        self.forward(-20)
