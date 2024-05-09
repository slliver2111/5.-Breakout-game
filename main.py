# TODO 1. Modularize More Clearly
# Although you have split components into different classes (like Paddle, Ball, Wall), your main game function game() is quite lengthy and mixes different layers of logic. Consider breaking it down into smaller functions or methods within appropriate classes.
#
# TODO 2. Manage Game State Better
# You are using a global variable game_is_on to control the game loop from outside the game() function. It's better to manage this within the game function itself, unless there's a specific reason to control it externally.
#
# TODO 5. Efficient Collision Detection
# The current collision detection mechanism might be inefficient as it checks every segment of every brick for every frame. Depending on how you've structured your bricks and segments, consider using more efficient collision detection algorithms or data structures like spatial hashing or bounding box checks.
#
# TODO 6. Enhance Responsiveness
# Currently, the game controls (Left, Right) might feel unresponsive due to the screen updates being tied to the game loop's speed. Consider adjusting the tracer settings or handling the input more asynchronously if possible.
#
# TODO 7. Error Handling
# There is no error handling around game logic. Including error handling can prevent the game from crashing unexpectedly and can provide better user feedback.
#
# TODO 8. Simplify the Exit Mechanism
# Using screen.exitonclick() forces the player to click the window to close it, which might not be intuitive if the game has already displayed a "You won!" or "Game over!" message. Consider adding a key binding to exit the game cleanly.
#
# TODO 9. Consider Adding Comments
# Adding comments to complex sections of your code can make it easier for other developers—or even your future self—to understand why certain decisions were made.


from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from title_board import TitleBoard
from lives_board import LivesBoard
import time
import math

GAME_SPEED = 50
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

NUMBER_OF_LIVES = 3


def detect_paddle_miss(ball):
    return ball.ycor() < -ball.vertical_limit


def detect_ball_left_right_edge_collision(ball):
    return math.fabs(ball.xcor()) > ball.horizon_limit


def detect_ball_top_edge_collision(ball):
    return ball.ycor() > ball.vertical_limit


def check_collisions(ball, paddle, wall):
    if paddle.detect_collision(ball):
        ball.bounce_off_paddle()
    elif wall.detect_collision(ball):
        ball.bounce_off_wall()
        # wall.update_bricks()


def update_game_state(wall, title_board, lives_board):
    if wall.no_bricks_left():
        title_board.display_message("You won!")
        return True
    elif lives_board.no_lives_left():
        title_board.display_message("Game over!")
    return False


def detect_screen_edge_collisions(ball, lives_board):
    # Paddle missed, ball collided with the bottom of window
    if detect_paddle_miss(ball):
        lives_board.decrease_live()
        ball.reset()
    # Ball collided with the left or right edge of window
    elif detect_ball_left_right_edge_collision(ball):
        ball.bounce_left_right()
    # Ball collided with the top edge of window
    elif detect_ball_top_edge_collision(ball):
        ball.bounce_up_down()


def game_loop(screen, paddle, ball, wall, title_board, lives_board):
    while True:
        time.sleep(1 / GAME_SPEED)
        screen.update()
        ball.move()

        check_collisions(ball, paddle, wall)
        detect_screen_edge_collisions(ball, lives_board)
        if update_game_state(wall, title_board, lives_board):
            break


def start_game():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Breakout Game")
    screen.tracer(0)

    player_paddle = Paddle((0, -SCREEN_HEIGHT / 2 + 20), SCREEN_WIDTH)
    player_ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
    wall = Wall(SCREEN_WIDTH, SCREEN_HEIGHT)
    title_board = TitleBoard()
    lives_board = LivesBoard(pos=(-SCREEN_WIDTH / 2 + 120, -SCREEN_HEIGHT / 2 + 40), lives=NUMBER_OF_LIVES)

    screen.listen()
    screen.onkey(player_paddle.left, "Left")
    screen.onkey(player_paddle.right, "Right")

    game_loop(screen, player_paddle, player_ball, wall, title_board, lives_board)
    screen.exitonclick()


if __name__ == '__main__':
    start_game()
