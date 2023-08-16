"""Module to store off the maze itself."""

import time

from window.cell import Cell
from window.window import Point


class Maze:
    """Object to store the maze window and attributes."""

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        """Initialize the maze itself."""
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        """Create the cells for the maze."""
        self._cells = [[self._draw_cell(col, row) for row in range(self._num_rows)] for col in range(self._num_cols)]

    def _draw_cell(self, col, row):
        """Draw out the individual cell given the column and row it represents."""
        top_left = Point(self._x1 + (col * self._cell_size_x), self._y1 + (row * self._cell_size_y))
        bottom_right = Point(self._x1 + ((col + 1) * self._cell_size_x), self._y1 + ((row + 1) * self._cell_size_y))

        cell = Cell(top_left, bottom_right, self._win)

        cell.draw(top_left, bottom_right)
        self._animate()

        return cell

    def _animate(self):
        """Animate the cell and pause for a period."""
        self._win.redraw()
        time.sleep(0.05)
