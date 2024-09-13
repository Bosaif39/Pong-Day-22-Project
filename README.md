# Snake Game

## Overview
This is the day 21 & 22 project of the course 100 Days of Code: The Complete Python Pro Bootcamp.This project is a classic Snake game, a popular programming exercise and a staple in game development. It demonstrates basic principles of game development using Python's `turtle` graphics library.

## How It Works
In this game, the player controls a snake that moves around the screen, consuming food to grow longer. The goal is to avoid collisions with the walls and the snake's own tail while aiming to achieve the highest possible score. The game ends when the snake collides with the wall or itself.

## Game Components

### 1. `food.py`
This file defines the `Food` class, which represents the food object the snake will eat. The `Food` class is derived from `Turtle` and includes:
- **Initialization (`__init__`)**: Sets up the food's appearance and initial position.
- **`newfood` method**: Randomly places the food on the screen.

### 2. `scoore.py`
This file defines the `Scoore` class, which manages the game's score. The `Scoore` class is derived from `Turtle` and includes:
- **Initialization (`__init__`)**: Sets up the score display.
- **`update_s` method**: Updates the displayed score.
- **`newscoore` method**: Increments the score and updates the display.
- **`gameover` method**: Displays a game over message.

### 3. `snake.py`
This file defines the `Snake` class, which represents the snake in the game. The `Snake` class includes:
- **Initialization (`__init__`)**: Creates the initial snake with a set number of segments.
- **`create_snake` method**: Initializes the snake with a starter configuration.
- **`move` method**: Moves the snake forward and updates the position of each segment.
- **Movement control methods (`up`, `down`, `right`, `left`)**: Change the direction of the snake.
- **`adder` method**: Adds a new segment to the snake.
- **`big` method**: Grows the snake by adding a new segment.

### 4. `main.py`
This is the main file that runs the game. It:
- Sets up the game screen using `turtle.Screen`.
- Initializes game objects (snake, food, and score).
- Handles user input to control the snake.
- Contains the main game loop that updates the game state, checks for collisions, and manages game over conditions.
- Offers the option to restart the game after a game over.


## Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)

## **Example**

![alt text](https://github.com/Bosaif39/example-pics/blob/main/D_20_21.png?raw=true)

