from turtle import Turtle

PADDLE_LENGTH = 8
PADDLE_STEP = 50
COLLISION_MARGIN = 20


class Paddle:
    def __init__(self, start_pos=(0, 0), screen_width=1000):
        self.paddle_segments = []
        self.limit_horizontal = screen_width / 2
        self.create_paddle(start_pos)
        self.center = self.paddle_segments[int(len(self.paddle_segments) / 2)]

    def create_paddle(self, start_pos):
        start_positions = [(start_pos[0] + i * 20, start_pos[1]) for i in range(PADDLE_LENGTH)]
        for pos in start_positions:
            segm = Turtle("square")
            segm.color("white")
            segm.penup()
            segm.setpos(pos)
            self.paddle_segments.append(segm)

    def left(self):
        if self.paddle_segments[0].xcor() > -self.limit_horizontal + 40:
            for segm in self.paddle_segments:
                segm.backward(PADDLE_STEP)

    def right(self):
        if self.paddle_segments[-1].xcor() < self.limit_horizontal - 50:
            for segm in self.paddle_segments:
                segm.forward(PADDLE_STEP)

    def detect_collision(self, ball):
        for segment in self.paddle_segments:
            if segment.distance(ball) < COLLISION_MARGIN:
                return True
        return False
