from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.velocity)    
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 360 or ball.distance(l_paddle) < 50 and -330 > ball.xcor() > -360:
        ball.bounce_x()
    
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.left_score()
    
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.right_score()

screen.exitonclick()