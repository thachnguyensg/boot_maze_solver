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
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win, top_left, bottom_right):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win
    def draw(self):
        if self.has_left_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            self._win.draw_line(Line(start, end), "black")
        if self.has_right_wall:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            self._win.draw_line(Line(start, end), "black")
        if self.has_top_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            self._win.draw_line(Line(start, end), "black")
        if self.has_bottom_wall:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            self._win.draw_line(Line(start, end), "black")


