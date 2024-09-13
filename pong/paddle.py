from turtle import Turtle

class Paddle(Turtle):
    """
    Represents a paddle in the Pong game. Inherits from Turtle and handles paddle movement.
    """

    def __init__(self, position):
        """
        Initializes the paddle with the following settings:
        - Shape: Square
        - Color: White
        - Size: Stretched to width of 5 units and height of 1 unit
        - Initial Position: Provided as an argument
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup() 
        self.goto(position)

    def go_up(self):
        """
        Moves the paddle up by 20 units.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the paddle down by 20 units.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
