"""Module to render individual cells."""

from window.window import Point, Line


class Cell:
    """Define an individual cell on the canvas."""

    def __init__(self, p1, p2, window):
        """Initialize a given cell with the Point and Window objects."""
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y

        self._win = window

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    def draw(self, top_left, bottom_right):
        """Draw out the cell using the top-left Point and bottom-right Point given."""
        if self.has_left_wall:
            line = Line(top_left, Point(top_left.x, bottom_right.y))
            self._win.draw_line(line, "green")

        if self.has_right_wall:
            line = Line(Point(bottom_right.x, top_left.y), bottom_right)
            self._win.draw_line(line, "blue")

        if self.has_top_wall:
            line = Line(top_left, Point(bottom_right.x, top_left.y))
            self._win.draw_line(line, "yellow")

        if self.has_bottom_wall:
            line = Line(Point(top_left.x, bottom_right.y), bottom_right)
            self._win.draw_line(line, "red")

    def draw_move(self, to_cell, undo=False):
        """Draw out a move from one cell to another."""
        color = "red"
        if undo:
            color = "gray"

        line_start = Point((self.x1 + (abs(self.x1 - self.x2) // 2)), (self.y1 + (abs(self.y1 - self.y2) // 2)))
        line_end = Point((to_cell.x1 + (abs(to_cell.x1 - to_cell.x2) // 2)), (to_cell.y1 + (abs(to_cell.y1 - to_cell.y2) // 2)))

        self._win.draw_line(Line(line_start, line_end), color)
