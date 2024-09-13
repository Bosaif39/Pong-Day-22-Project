
# Pong Game

## Overview

This is the Day 22 project from the "100 Days of Code: The Complete Python Pro Bootcamp." This classic Pong game simulation showcases basic game development concepts using Python's `turtle` module. The game features two paddles, a ball, and a scoreboard, all interacting in a fun and competitive way.

## How It Works

The Pong game is a two-player game where each player controls a paddle to hit a ball back and forth. The game mechanics include:

- **Ball Movement:** The ball moves continuously across the screen, bouncing off the paddles and walls.
- **Paddle Movement:** Players use keyboard controls to move their paddles up and down to hit the ball.
- **Scoring:** When the ball passes a paddle, the opposing player scores a point, and the ball resets to the center.

## Game Components

### 1. `ball.py`

Defines the `Ball` class, which handles the ball's movement, collision with paddles and walls, and resetting its position.

- **Methods:**
  - `__init__()`: Initializes the ball’s properties such as color, shape, movement speed, and direction.
  - `move()`: Updates the ball’s position based on its speed.
  - `bounce_y()`: Reverses the ball’s vertical direction.
  - `bounce_x()`: Reverses the ball’s horizontal direction and increases its speed slightly.
  - `reset_position()`: Resets the ball to the center and adjusts its direction and speed.

### 2. `paddle.py`

Defines the `Paddle` class, which represents each player's paddle and handles paddle movement.

- **Methods:**
  - `__init__(position)`: Initializes the paddle’s appearance, size, and position.
  - `go_up()`: Moves the paddle up by 20 units.
  - `go_down()`: Moves the paddle down by 20 units.

### 3. `scoreboard.py`

Defines the `Scoreboard` class, which manages the display and updating of the game scores.

- **Methods:**
  - `__init__()`: Initializes the scoreboard and sets initial scores.
  - `update_scoreboard()`: Updates the display to show the current scores.
  - `l_point()`: Increments the left paddle’s score and updates the scoreboard.
  - `r_point()`: Increments the right paddle’s score and updates the scoreboard.

### 4. `main.py`

Sets up the game environment, including the screen, paddles, ball, and scoreboard. Manages game logic and interactions between components.

- **Functionality:**
  - Configures the screen and initializes game components.
  - Sets up keyboard controls for paddle movement.
  - Runs the game loop, handling ball movement, collision detection, and scoring.
  - Updates the screen continuously and exits when clicked.

## Requirements

- **Python 3.x**: Ensure you have Python 3.x installed on your machine.
- **`turtle` module**: This module is included with Python’s standard library.

## **Example**

![alt text]()





