from turtle import Screen
from paddle import Paddle
from ball import Ball

import math
import time

GAME_SPEED = 0.01
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


def game():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Breakout Game")
    screen.tracer(0)

    user_paddle = Paddle((0, -SCREEN_HEIGHT / 2 + 20), SCREEN_WIDTH)
    ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
    # scoreboard = Scoreboard((0, screen.window_height() / 2 - 80))

    screen.listen()
    screen.onkey(user_paddle.left, "a")
    screen.onkey(user_paddle.right, "d")

    while True:
        screen.update()
        ball.move_ball()

        # check_wall_collision(self):
        if math.fabs(ball.ycor()) > ball.vertical_limit:
            ball.bounce_up_down()

        # check goal:
        if ball.xcor() > SCREEN_WIDTH / 2:
            ball.bounce_left_right()
            ball.reset_ball()
            # scoreboard.add_point_left()
        elif ball.xcor() < -SCREEN_WIDTH / 2:
            ball.bounce_left_right()
            ball.reset_ball()
            # scoreboard.add_point_right()

        time.sleep(GAME_SPEED)

        # check_paddle_hit_ball:
        for segm in user_paddle.paddle_segments:
            if segm.distance(ball) < 20:
                ball.bounce_left_right()
                break

        for segm in user_paddle.paddle_segments:
            if segm.distance(ball) < 20:
                ball.bounce_left_right()
                break


if __name__ == '__main__':
    game_is_on = True
    while game_is_on:
        game()
