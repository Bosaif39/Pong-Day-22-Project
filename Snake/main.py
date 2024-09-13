from snake import Snake
from food import Food
from scoore import Scoore
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoore = Scoore()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

def reset_game():
    global snake, food, scoore
    screen.clear()  # Clears everything on the screen
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()  # Re-create the snake object
    food = Food()    # Re-create the food object
    scoore = Scoore()  # Re-create the score object

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")



game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #make the snake biger when he eat food
    if snake.head.distance(food) < 15:
        food.newfood()
        snake.big()
        scoore.newscoore()

    # Detect Collisions with the walls
    if (snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300):
        scoore.gameover()
        game = False

        #restart if the player want
        play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no)").lower()
        if play_again == "yes":
            game = True
            reset_game()



    # Detect Collisions with your own Tail
    # Only start checking for collisions if the snake has grown beyond its initial size
    if len(snake.parts) > 3:
        for segment in snake.parts[1:]:  # Skipping the head, starting from the second segment
            if snake.head.distance(segment) < 10:  # Distance threshold for collision
                game = False
                scoore.gameover()

                #restart if the player want
                play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no)").lower()
                if play_again == "yes":
                    game = True
                    reset_game()

screen.exitonclick()
