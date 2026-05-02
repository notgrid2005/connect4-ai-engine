"""Minimax AI with Alpha-Beta Pruning for Connect4."""
import math
from .board import Board, ROWS, COLS, EMPTY, PLAYER, AI


def score_window(window, piece):
    opp = PLAYER if piece == AI else AI
    score = 0
    pc = list(window).count(piece)
    ec = list(window).count(EMPTY)
    oc = list(window).count(opp)
    if pc == 4:
        score += 100
    elif pc == 3 and ec == 1:
        score += 5
    elif pc == 2 and ec == 2:
        score += 2
    if oc == 3 and ec == 1:
        score -= 4
    return score


def evaluate(board, piece):
    score = 0
    g = board.grid
    # Center column preference
    center = [int(g[r][COLS // 2]) for r in range(ROWS)]
    score += center.count(piece) * 3
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            score += score_window(g[r][c:c+4], piece)
    # Vertical
    for c in range(COLS):
        col_arr = [g[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            score += score_window(col_arr[r:r+4], piece)
    # Diagonals
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            score += score_window([g[r+i][c+i] for i in range(4)], piece)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            score += score_window([g[r-i][c+i] for i in range(4)], piece)
    return score


def minimax(board, depth, alpha, beta, maximizing):
    valid = board.valid_columns()
    is_terminal = board.check_win(PLAYER) or board.check_win(AI) or board.is_full()
    if depth == 0 or is_terminal:
        if is_terminal:
            if board.check_win(AI):
                return None, math.inf
            elif board.check_win(PLAYER):
                return None, -math.inf
            else:
                return None, 0
        return None, evaluate(board, AI)

    if maximizing:
        value = -math.inf
        best_col = valid[0]
        for col in valid:
            temp = board.copy()
            temp.drop_piece(col, AI)
            _, new_score = minimax(temp, depth - 1, alpha, beta, False)
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = valid[0]
        for col in valid:
            temp = board.copy()
            temp.drop_piece(col, PLAYER)
            _, new_score = minimax(temp, depth - 1, alpha, beta, True)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value


def get_ai_move(board, depth=5):
    col, _ = minimax(board, depth, -math.inf, math.inf, True)
    return col
