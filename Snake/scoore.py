from turtle import Turtle

class Scoore(Turtle):
    """
    The Scoore class manages the game's score.
    Inherits from Turtle.
    """
    
    def __init__(self):
        """
        Initialize the Scoore object:
        - Hides the turtle.
        - Sets the color to white.
        - Positions the score display at the top of the screen.
        - Initializes the score to 0.
        - Updates the score display.
        """
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_s()

    def update_s(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))

    def newscoore(self):
        self.score += 1
        self.clear()
        self.update_s()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
