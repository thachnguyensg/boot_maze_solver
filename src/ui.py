from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        print("Waiting for window to close")
        self.running = True
        self.redraw()
        self.__root.mainloop()

    def close(self):
        print("Closing window")
        self.running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        left_wall_start = Point(self._x1, self._y1)
        left_wall_end = Point(self._x1, self._y2)
        left_wall_color = "black"
        if not self.has_left_wall:
            left_wall_color = "white"
        self._win.draw_line(Line(left_wall_start, left_wall_end), left_wall_color)

        right_wall_start = Point(self._x2, self._y1)
        right_wall_end = Point(self._x2, self._y2)
        right_wall_color = "black"
        if not self.has_right_wall:
            right_wall_color = "white"
        self._win.draw_line(Line(right_wall_start, right_wall_end), right_wall_color)

        top_wall_start = Point(self._x1, self._y1)
        top_wall_end = Point(self._x2, self._y1)
        top_wall_color = "black"
        if not self.has_top_wall:
            top_wall_color = "white"
        self._win.draw_line(Line(top_wall_start, top_wall_end), top_wall_color)

        bottom_wall_start = Point(self._x1, self._y2)
        bottom_wall_end = Point(self._x2, self._y2)
        bottom_wall_color = "black"
        if not self.has_bottom_wall:
            bottom_wall_color = "white"
        self._win.draw_line(Line(bottom_wall_start, bottom_wall_end), bottom_wall_color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        start = Point((self._x2 + self._x1) // 2, (self._y2 + self._y1) // 2)
        end = Point((to_cell._x2 + to_cell._x1) // 2, (to_cell._y2 + to_cell._y1) // 2)
        color = "red"
        if undo:
            color = "gray"
        self._win.draw_line(Line(start, end), color)
