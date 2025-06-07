from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from ScoreCard import ScoreCard
import time

pong = Turtle()
screen = Screen()
ball = Ball()
score = ScoreCard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

Game_Mood = True
while Game_Mood:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball is collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Ball is collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # right paddle misses ball 
    if ball.xcor() > 380:
        ball.reset()
        score.l_paddle_score()

    # left paddle misses ball 
    if ball.xcor() < -380:
        ball.reset()
        score.r_paddle_score()


screen.exitonclick()