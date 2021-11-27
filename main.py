import time
from turtle import Screen

from ball import Ball
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WALL_BOUNCE_Y_COR, PADDLE_X_DELTA_BOUNCE, \
    RIGHT_PADDLE_X_POSITION, LEFT_PADDLE_X_POSITION, LEFT_PLAYER_KEY_UP, LEFT_PLAYER_KEY_DOWN, RIGHT_PLAYER_KEY_UP, \
    RIGHT_PLAYER_KEY_DOWN, WIN_SCORE
from paddle import Paddle

# TODO№1 Мяч появляется в рандомном месте на 0 по у
from scoreboard import Scoreboard

game_on = True

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

player_left = Paddle(1)
player_right = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_left.up, LEFT_PLAYER_KEY_UP)
screen.onkey(player_left.down, LEFT_PLAYER_KEY_DOWN)
screen.onkey(player_right.up, RIGHT_PLAYER_KEY_UP)
screen.onkey(player_right.down, RIGHT_PLAYER_KEY_DOWN)

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Continuous paddle move version
    # player_1.move()
    # player_2.move()
    # if player_1.ycor() > PADDLE_STOP_Y_COR or player_1.ycor() < -PADDLE_STOP_Y_COR:
    #     player_1.stop()
    # if player_2.ycor() > PADDLE_STOP_Y_COR or player_2.ycor() < -PADDLE_STOP_Y_COR:
    #     player_2.stop()

    # Detect collision with wall and bounce
    if ball.ycor() > WALL_BOUNCE_Y_COR or ball.ycor() < -WALL_BOUNCE_Y_COR:
        ball.bounce_from_wall()

    # Detect paddle collision with right player and bounce
    if ball.distance(player_right) < 50 and ball.xcor() > RIGHT_PADDLE_X_POSITION - PADDLE_X_DELTA_BOUNCE:
        ball.bounce_from_paddle(paddle_y=player_right.ycor())

    if ball.distance(player_left) < 50 and ball.xcor() < LEFT_PADDLE_X_POSITION + PADDLE_X_DELTA_BOUNCE:
        ball.bounce_from_paddle(paddle_y=player_left.ycor())

    # if ball.distance(player_right) < 50 and ball.xcor() > RIGHT_PADDLE_X_POSITION - PADDLE_X_DELTA_BOUNCE:

    # Left player scores a point
    if ball.xcor() > RIGHT_PADDLE_X_POSITION + 10:
        scoreboard.left_point()
        ball.refresh(heading='left')

    # Right player scores a point
    if ball.xcor() < LEFT_PADDLE_X_POSITION - 10:
        scoreboard.right_point()
        ball.refresh(heading='right')

    if scoreboard.right_score == WIN_SCORE or scoreboard.left_score == WIN_SCORE:
        scoreboard.game_over()
        game_on = False


screen.exitonclick()
