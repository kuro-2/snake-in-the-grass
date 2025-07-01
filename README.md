# Snake in the Grass

This project is a simple Snake game made for fun and for learning the basics of [Pygame](https://www.pygame.org/). The game features a colorful interface, adjustable speed, and a background image. You can pause and resume the game, and your score is displayed on the screen.

## About Pygame

Pygame is a set of Python modules designed for writing video games. It provides functionalities for rendering graphics, playing sounds, handling user input, and more. Pygame works by creating a window (the display surface), drawing shapes or images onto it, and updating the display in a loop. User input (like keyboard or mouse events) is handled through an event queue.

In this project, Pygame is used to:
- Create the game window and handle drawing (`pygame.display`)
- Draw shapes and images for the snake, apple, and background
- Handle keyboard input for controlling the snake and pausing the game
- Manage the game loop and timing

## How to Run

1. Install the requirements:
   ```sh
   pip install -r requirements.txt
   ```
2. Make sure you have `image1.png` in the same directory as `main.py`.
3. Run the game:
   ```sh
   python main.py
   ```

## How to Make Your Own Snake Game

You can use this code as a starting point for your own Snake game. Here are some ideas to customize or extend it:
- Change the colors, images, or grid size by modifying the configuration section at the top of `main.py`.
- Add new features, such as obstacles, power-ups, or different game modes.
- Replace the background image with your own by changing the file loaded in `bg_image`.
- Modify the scoring system or add a high score tracker.
- Experiment with the snake's movement, speed, or controls.

Explore the code and try making your own changes to learn more about how Pygame works!

## Controls

- Arrow keys: Move the snake
- P: Pause/Resume
- Q: Quit

Enjoy playing and learning!

Some Screenshot of game: 
![image](https://github.com/user-attachments/assets/b818aa4d-68ce-4568-a733-c82196443dbb)



