from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from title_board import TitleBoard
from lives_board import LivesBoard

import math
import time

GAME_SPEED = 50
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

NUMBER_OF_LIVES = 3


def game():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Breakout Game")
    screen.tracer(0)

    user_paddle = Paddle((0, -SCREEN_HEIGHT / 2 + 20), SCREEN_WIDTH)
    ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
    wall = Wall(SCREEN_WIDTH, SCREEN_HEIGHT)
    title_board = TitleBoard()
    lives_board = LivesBoard(pos=(-SCREEN_WIDTH / 2 + 120, -SCREEN_HEIGHT / 2 + 40), lives=NUMBER_OF_LIVES)

    screen.listen()
    screen.onkey(user_paddle.left, "Left")
    screen.onkey(user_paddle.right, "Right")

    def check_if_win():
        return len(wall.box) == 0

    def check_if_lost():
        return lives_board.get_lives() == 0

    def detect_brick_collision():
        for brick in wall.box:
            for segment in brick.brick_segments:
                if ball.distance(segment) < 20:
                    brick.kill()
                    wall.box.remove(brick)
                    return True
        return False

    def detect_paddle_miss():
        return ball.ycor() < -ball.vertical_limit

    def detect_ball_left_right_edge_collision():
        return math.fabs(ball.xcor()) > ball.horizon_limit

    def detect_ball_top_edge_collision():
        return ball.ycor() > ball.vertical_limit

    def detect_ball_paddle_collision():
        for segment in user_paddle.paddle_segments:
            if segment.distance(ball) < 20:
                return True
        return False

    while True:
        time.sleep(1 / GAME_SPEED)
        screen.update()
        ball.move_ball()

        if check_if_win():
            title_board.update_text("You won!")
            break
        elif check_if_lost():
            title_board.update_text("Game over!")
            break

        if detect_paddle_miss():
            lives_board.decrease_live()
            ball.reset_ball()
        elif detect_brick_collision() or detect_ball_paddle_collision() or detect_ball_top_edge_collision():
            ball.bounce_up_down()
        elif detect_ball_left_right_edge_collision():
            ball.bounce_left_right()

    screen.exitonclick()


if __name__ == '__main__':
    game_is_on = True
    while game_is_on:
        game()
