from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.score = 0

        self.score_display()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.score_display()

    def game_over(self, winner):
        self.goto(0, 100)
        self.write(f"{winner} wins!", move=False,
                   align=ALIGNMENT, font=FONT)

    def score_display(self):
        self.write(f"Score:{self.score}", move=False,
                   align=ALIGNMENT, font=FONT)
