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

