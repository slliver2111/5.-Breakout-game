from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_STEP = 50


class Paddle:
    def __init__(self, start_pos=(0, 0), screen_height=600):
        self.paddle_segments = []
        self.limit_vertical = screen_height / 2
        self.create_paddle(start_pos)
        self.center = self.paddle_segments[int(len(self.paddle_segments) / 2)]

    def create_paddle(self, start_pos):
        start_positions = [(start_pos[0], start_pos[1] + i * 20) for i in range(PADDLE_LENGTH)]
        for pos in start_positions:
            segm = Turtle("square")
            segm.color("white")
            segm.penup()
            segm.setpos(pos)
            segm.setheading(90)
            self.paddle_segments.append(segm)

    def left(self):
        if self.paddle_segments[-1].ycor() < self.limit_vertical - 20:
            for segm in self.paddle_segments:
                segm.left(PADDLE_STEP)

    def right(self):
        if self.paddle_segments[0].ycor() > -self.limit_vertical + 40:
            for segm in self.paddle_segments:
                segm.right(PADDLE_STEP)
