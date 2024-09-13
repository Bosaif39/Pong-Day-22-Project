from turtle import Turtle
import random

class Food(Turtle):
    """
    The Food class represents the food object in the game.
    Inherits from Turtle.
    """
    
    def __init__(self):
        """
        Initialize the Food object:
        - Sets the shape to a circle.
        - Hides the pen and sets the color to red.
        - Sets the speed to the fastest.
        - Places the food at a new random location.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.newfood()

    def newfood(self):
        """
        Randomly place the food at a new position on the screen.
        Coordinates are within the range (-280, 280) for both x and y.
        """
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
