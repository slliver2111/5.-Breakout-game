from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 44, 'normal')


class LivesBoard(Turtle):
    def __init__(self, pos=(0, 0), lives=3):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.lives = lives
        self.start_lives = lives
        self.update()

    def decrease_live(self):
        self.lives -= 1
        self.update()

    def reset(self):
        self.lives = self.start_lives

    def update(self):
        self.clear()
        self.write(f"Lives: {self.lives}", False, align=ALIGNMENT, font=FONT)

    def get_lives(self):
        return self.lives
