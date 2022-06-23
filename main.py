from turtle import Screen, Turtle, position

from pyparsing import line
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# SETTING UP THE SCREEN
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")

# used to turn turtle animation on or off and set a delay for update drawings
my_screen.tracer(0)

# SETTING UP THE BATTLE FIELD
line_turtle = Turtle()
line_turtle.penup()
line_turtle.color("white")
line_turtle.goto(0, 300)
line_turtle.pendown()
line_turtle.goto(0, -300)
line_turtle.penup()
line_turtle.hideturtle()


# Left and Right paddle being created.
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

# CREATING THE BALL
ball = Ball()

# CREATING THE SCORE
r_score = Scoreboard((200, 280))
l_score = Scoreboard((-200, 280))

# LISTENING TO KEY STROKES
my_screen.listen()
my_screen.onkeypress(r_paddle.move_up, "Up")
my_screen.onkeypress(r_paddle.move_down, "Down")
my_screen.onkeypress(l_paddle.move_up, "w")
my_screen.onkeypress(l_paddle.move_down, "s")

game_status = True
while game_status:
    time.sleep(ball.time_delay)
    my_screen.update()
    ball.move()

    # Check the winner as soon the score reaches 10!
    if l_score.score == 10:
        game_status = False
        l_score.game_over("Left")
        line_turtle.clear()
    elif r_score.score == 10:
        r_score.game_over("Right")
        game_status = False
        line_turtle.clear()

    # DETECT COLLISON WITH TOP AND BOTTOM WALL
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.y_bounce()
    # DETECT COLLISION WITH LEFT AND RIGHT WALL
    if(ball.xcor() > 400):
        ball.reset()
        l_score.increment_score()

    if(ball.xcor() < -400):
        ball.reset()
        r_score.increment_score()

    # DETECT COLLISION WITH PADDLES
    if(ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.x_bounce()


my_screen.exitonclick()
