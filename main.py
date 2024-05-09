#TODO 1. Modularize More Clearly
# Although you have split components into different classes (like Paddle, Ball, Wall), your main game function game() is quite lengthy and mixes different layers of logic. Consider breaking it down into smaller functions or methods within appropriate classes.
#
#TODO 2. Manage Game State Better
# You are using a global variable game_is_on to control the game loop from outside the game() function. It's better to manage this within the game function itself, unless there's a specific reason to control it externally.
#
#TODO 3. Use More Descriptive Variable Names
# Some variable names like box in wall.box are not very descriptive. Consider renaming these to more clearly represent their function, like bricks for a collection of brick objects in the wall.
#
#TODO 4. Avoid Magic Numbers
# There are numbers like 20, 22, etc., in collision detection that appear magical and unexplained. Define these as constants at the top of your file to make the code more readable and easier to maintain.
#
#TODO 5. Efficient Collision Detection
# The current collision detection mechanism might be inefficient as it checks every segment of every brick for every frame. Depending on how you've structured your bricks and segments, consider using more efficient collision detection algorithms or data structures like spatial hashing or bounding box checks.
#
#TODO 6. Enhance Responsiveness
# Currently, the game controls (Left, Right) might feel unresponsive due to the screen updates being tied to the game loop's speed. Consider adjusting the tracer settings or handling the input more asynchronously if possible.
#
#TODO 7. Error Handling
# There is no error handling around game logic. Including error handling can prevent the game from crashing unexpectedly and can provide better user feedback.
#
#TODO 8. Simplify the Exit Mechanism
# Using screen.exitonclick() forces the player to click the window to close it, which might not be intuitive if the game has already displayed a "You won!" or "Game over!" message. Consider adding a key binding to exit the game cleanly.
#
#TODO 9. Consider Adding Comments
# Adding comments to complex sections of your code can make it easier for other developers—or even your future self—to understand why certain decisions were made.


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
            if segment.distance(ball) < 22:
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
