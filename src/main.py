from ui import Window, Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 600)

    # start = Point(100, 100)
    # end = Point(200, 100)
    # win.draw_line(Line(start, end), "black")

    # cell1 = Cell(win)
    # cell1.draw(150, 150, 200, 200)
    #
    # cell2 = Cell(win)
    # cell2.has_left_wall = False
    # cell2.draw(210, 150, 250, 200)
    #
    # cell1.draw_move(cell2, True)

    maze = Maze(100, 100, 5, 5, 50, 50, win)

    win.wait_for_close()


main()
