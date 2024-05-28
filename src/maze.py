from ui import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed

        self._create_cells()
        self._break_entrance_and_exit()
        print("start breaking")
        self._break_cell_r(0, 0)
        print("done breaking")

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cells(0, 0)
        exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit.has_bottom_wall = False
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)

    def _break_cell_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        print(f"Breaking cell {i}, {j}")
        while True:
            directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if i - 1 < 0 or self._cells[i - 1][j].visited:
                directions.remove((i - 1, j))
            if i + 1 >= self._num_rows or self._cells[i + 1][j].visited:
                directions.remove((i + 1, j))
            if j - 1 < 0 or self._cells[i][j - 1].visited:
                directions.remove((i, j - 1))
            if j + 1 >= self._num_cols or self._cells[i][j + 1].visited:
                directions.remove((i, j + 1))

            if len(directions) == 0:
                return

            if self._seed is not None:
                random.seed(self._seed)
            next_direction = random.choice(directions)

            next_i, next_j = next_direction
            next_cell = self._cells[next_i][next_j]
            if next_i < i:
                current.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_i > i:
                current.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_j < j:
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_j > j:
                current.has_bottom_wall = False
                next_cell.has_top_wall = False
            self._draw_cells(i, j)
            self._draw_cells(next_i, next_j)
            current.draw_move(next_cell)
            self._break_cell_r(next_i, next_j)
