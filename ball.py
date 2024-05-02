import math
from turtle import Turtle

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.horizon_limit = screen_width / 2
        self.vertical_limit = screen_height / 2 - 30
        self.up_down = -3
        self.left_right = -3

    def move_ball(self):
        new_xcor = self.xcor() + self.left_right
        new_ycor = self.ycor() + self.up_down
        self.goto(new_xcor, new_ycor)
        # self.forward(self.left_right * BALL_SPEED)
        # self.left(self.up_down * 90)
        # self.forward(BALL_SPEED)
        # self.right(self.up_down * 90)

    def bounce_left_right(self):
        self.left_right *= -1

    def bounce_up_down(self):
        self.up_down *= -1

    def reset_ball(self):
        self.goto(0, 0)
