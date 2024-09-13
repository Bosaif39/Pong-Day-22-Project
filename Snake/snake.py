from turtle import Turtle

DISTANCE = 20
STARTER = [(0, 0), (20, 0), (40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    The Snake class represents the snake in the game.
    Manages the snake's movement and growth.
    """
    
    def __init__(self):
        """
        Initialize the Snake object:
        - Create the snake with initial segments.
        - Set the head of the snake as the first segment.
        """
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        """
        Create the initial snake with a set number of segments.
        """
        for i in STARTER:
            self.adder(i)

    def move(self):
        """
        Move the snake forward:
        - Update the position of each segment to follow the one before it.
        - Move the head forward by a set distance.
        """
        for index in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[index - 1].xcor()
            new_y = self.parts[index - 1].ycor()
            self.parts[index].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        """
        Change the direction of the snake to up, if it's not already moving down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Change the direction of the snake to down, if it's not already moving up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """
        Change the direction of the snake to right, if it's not already moving left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """
        Change the direction of the snake to left, if it's not already moving right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def adder(self, i):
        """
        Add a new segment to the snake at the specified position.
        - Creates a new turtle segment.
        - Appends the segment to the snake's list of parts.
        
        Args:
        - position (tuple): The (x, y) coordinates where the new segment should be placed.
        """
        p1 = Turtle("square")
        p1.color("white")
        p1.penup()
        p1.goto(i)
        self.parts.append(p1)

    def big(self):
        """
        Grow the snake by adding a new segment at the position of the last segment.
        """
        self.adder(self.parts[-1].position())
