from ui import Window, Point, Line, Cell
def main():
    win = Window(800, 600)

    start = Point(100, 100)
    end = Point(200, 100)
    win.draw_line(Line(start, end), "black")

    cell1 = Cell(win, Point(150, 150), Point(200, 200))
    cell1.draw()

    cell2 = Cell(win, Point(210, 150), Point(250, 200))
    cell2.has_left_wall = False
    cell2.draw()


    win.wait_for_close()

main()
