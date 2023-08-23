"""Module to run the Maze Runner program."""

from window.cell import Cell
from window.window import Line, Point, Window

from window.maze import Maze


if __name__ == "__main__":
    new_maze = Window(800, 800)

#    # first line
#    point_one = Point(10, 10)
#    point_two = Point(45, 95)
#
#    line = Line(point_one, point_two)
#
#    new_maze.draw_line(line, "blue")
#
#    # second line
#    point_three = Point(650, 450)
#    point_four = Point(650, 150)
#
#    line_two = Line(point_three, point_four)
#
#    new_maze.draw_line(line_two, "red")
#
#    # cell one
#    cell_one = Cell(point_one, point_two, new_maze)
#    cell_one.draw(point_one, point_four)
#
#    # draw a move between cells
#
#    cell_one_point_one = Point(250, 250)
#    cell_one_point_two = Point(275, 275)
#    cell_start = Cell(cell_one_point_one, cell_one_point_two, new_maze)
#    cell_start.draw(cell_one_point_one, cell_one_point_two)
#
#    cell_two_point_one = Point(275, 275)
#    cell_two_point_two = Point(300, 300)
#    cell_end = Cell(cell_two_point_one, cell_two_point_two, new_maze)
#    cell_end.draw(cell_two_point_one, cell_two_point_two)
#
#    cell_start.draw_move(cell_end, undo=True)

    new_new_maze = Maze(20, 20, 30, 30, 25, 25, new_maze)

    new_maze.wait_for_close()
