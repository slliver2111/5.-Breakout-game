from brick import Brick
import random

NUM_COLUMNS = 20
NUM_ROWS = 6
WIDTH = 200
COLLISION_MARGIN = 20


class Wall:
    def __init__(self, screen_width, screen_height):
        self.bricks = []
        self.screen_width = screen_width
        for i in range(NUM_ROWS):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            for j in range(NUM_COLUMNS - 5):
                x_cor = -screen_width / 2 + j * 60 + j * 5 + 20
                y_cor = screen_height / 2 - i * 25 - 20

                self.bricks.append(Brick(x_cor, y_cor, (r, g, b)))

    def generate_random_car(self):
        y_cor = random.randint(-WIDTH, WIDTH)
        self.bricks.append(Brick(self.screen_width / 2, y_cor))

    def detect_collision(self, ball):
        for brick in self.bricks:
            for segment in brick.brick_segments:
                if ball.distance(segment) < COLLISION_MARGIN:
                    brick.kill()
                    self.bricks.remove(brick)
                    return True
        return False

    def no_bricks_left(self):
        return len(self.bricks) == 0
