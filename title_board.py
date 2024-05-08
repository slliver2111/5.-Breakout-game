from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 88, 'normal')


class TitleBoard(Turtle):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(pos)

    def update_text(self, text):
        self.clear()
        self.write(f"{text}", False, align=ALIGNMENT, font=FONT)


