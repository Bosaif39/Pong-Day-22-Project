from turtle import Turtle

class Ball(Turtle):
    """
    Represents the ball in the Pong game. Inherits from Turtle and handles movement, collision, and resetting.
    """

    def __init__(self):
        """
        Initializes the ball with default settings:
        - Color: White
        - Shape: Circle
        - Movement: Initial x and y speed of 3 units
        - Move speed: 0.1
        """
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()  
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        """
        Moves the ball forward based on its x_move and y_move attributes.
        Updates the ball's position to a new x and y coordinate.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the direction of the ball's movement along the y-axis.
        This simulates a bounce when the ball hits the top or bottom wall.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the direction of the ball's movement along the x-axis.
        This simulates a bounce when the ball hits the paddle.
        Additionally, slightly increases the ball's speed by reducing move_speed.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Resets the ball's position to the center of the screen and speed to initial values.
        Also reverses the ball's x direction to restart the game.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
