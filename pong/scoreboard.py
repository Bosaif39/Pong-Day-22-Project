from turtle import Turtle

class Scoreboard(Turtle):
    """
    Manages the display of the game score. Inherits from Turtle.
    """

    def __init__(self):
        """
        Initializes the scoreboard:
        - Color: White
        - Hides the turtle
        - Sets initial scores for left and right paddles
        - Updates the scoreboard display
        """
        super().__init__()
        self.color("white")
        self.penup() 
        self.hideturtle()  
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the previous score and updates the scoreboard display with the current scores.
        """
        self.clear()  # Clears the previous score
        self.goto(-100, 200)  # Position for left score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # Position for right score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Increments the left paddle's score and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increments the right paddle's score and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()
