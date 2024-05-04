import turtle
from turtle import Turtle
import random

LENGTH = 3


class Brick:
    def __init__(self, start_x, start_y, color=(125, 125, 125)):
        self.brick_segments = []
        self.color = color
        turtle.colormode(255)
        self.create_brick(start_x, start_y)

    def create_brick(self, start_x, start_y):

        for i in range(LENGTH):
            segm = Turtle("square")
            segm.penup()
            segm.color(self.color)
            segm.goto(start_x + i * 20, start_y)
            segm.setheading(180)
            self.brick_segments.append(segm)

    def get_xcor(self):
        return self.brick_segments[0].xcor()

    def kill(self):
        for segm in self.brick_segments:
            segm.hideturtle()
            segm.clear()
