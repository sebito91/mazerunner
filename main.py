"""Module to run the Maze Runner program."""

from window.cell import Cell
from window.window import Line, Point, Window


if __name__ == "__main__":
    new_maze = Window(800, 600)

    # first line
    point_one = Point(10, 10)
    point_two = Point(45, 95)

    line = Line(point_one, point_two)

    new_maze.draw_line(line, "blue")

    # second line
    point_three = Point(650, 450)
    point_four = Point(650, 150)

    line_two = Line(point_three, point_four)

    new_maze.draw_line(line_two, "red")

    # cell one
    cell_one = Cell(point_one, point_two, new_maze)
    cell_one.draw(point_one, point_four)

    new_maze.wait_for_close()
