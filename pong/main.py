from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off screen updates for smoother animation


r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Move right paddle up
screen.onkey(r_paddle.go_down, "Down")  # Move right paddle down
screen.onkey(l_paddle.go_up, "w")  # Move left paddle up
screen.onkey(l_paddle.go_down, "s")  # Move left paddle down

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()  # Increment left paddle score

    # Detect if the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()  # Increment right paddle score

# Close the window when clicked
screen.exitonclick()
