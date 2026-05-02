"""Connect4 Board representation."""
import numpy as np

ROWS, COLS = 6, 7
EMPTY, PLAYER, AI = 0, 1, 2

class Board:
    def __init__(self):
        self.grid = np.zeros((ROWS, COLS), dtype=int)

    def drop_piece(self, col, piece):
        for r in range(ROWS - 1, -1, -1):
            if self.grid[r][col] == EMPTY:
                self.grid[r][col] = piece
                return r
        return -1

    def is_valid(self, col):
        return 0 <= col < COLS and self.grid[0][col] == EMPTY

    def valid_columns(self):
        return [c for c in range(COLS) if self.is_valid(c)]

    def check_win(self, piece):
        g = self.grid
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(g[r][c+i] == piece for i in range(4)):
                    return True
        for r in range(ROWS - 3):
            for c in range(COLS):
                if all(g[r+i][c] == piece for i in range(4)):
                    return True
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(g[r+i][c+i] == piece for i in range(4)):
                    return True
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(g[r-i][c+i] == piece for i in range(4)):
                    return True
        return False

    def is_full(self):
        return len(self.valid_columns()) == 0

    def copy(self):
        b = Board()
        b.grid = self.grid.copy()
        return b

    def __str__(self):
        symbols = {EMPTY: ".", PLAYER: "X", AI: "O"}
        header = " ".join(str(i) for i in range(COLS))
        rows = ["  ".join(symbols[c] for c in row) for row in self.grid]
        return header + "\n" + "\n".join(rows)
