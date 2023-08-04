"""Module to run the Maze Runner program."""

from window.window import Window


if __name__ == "__main__":
    new_maze = Window(800, 600)
    new_maze.wait_for_close()
