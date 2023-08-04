"""Module to represent a given window for the maze."""

from tkinter import Tk, Canvas, CENTER


class Window:
    """Widget to render a window for the maze object."""

    def __init__(self, width, height):
        """Initialize the maze window object."""
        self.__root = Tk()
        self.__window_running = False

        self.__root.title("Maze Runner in all its glory!")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, {"height": height, "width": width})
        self.__canvas.pack()

    def redraw(self):
        """Redraw the canvas object."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Keep the window alive and redraw until close received."""
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        """Close out the running window."""
        self.__window_running = False
