"""
Scores non-terminal board states by scanning every possible 4-cell window
(horizontal, vertical, both diagonals) and weighting based on piece composition.
Defensive blocking is prioritized since block an opponents 3 in-a-row is more
important than building our 2 in-a-row. Stopping defeat and delaying winning

"""

from board_logic import Connect4Board, ROWS, PLAYER_1, PLAYER_2


# --- Scoring weights tuned to determine a defensive or offensive next move---

FOUR_WEIGHT        = 100   # winning line
THREE_WEIGHT       = 10    # one move from winning
THREE_IMMEDIATE    = 25    # one move from winning AND that move is playable right now
TWO_WEIGHT         = 3     # building potential

OPP_THREE_WEIGHT    = -50   # opponent one move from winning
OPP_THREE_IMMEDIATE = -80   # opponent can win THIS turn
OPP_TWO_WEIGHT      = -2    # mild opponent threat

CENTER_WEIGHTS = [0, 1, 2, 3, 2, 1, 0]

COLS_RANGE = 7


def _score_window(cells: list[int], player: int, opponent: int,
                  heights: list[int]) -> int:
    """
    Score a single 4-cell window based on piece composition.

    When a window has exactly one empty cell (a potential completion),
    checks if that cell is the next piece that would land in its column
    (immediate threat) vs suspended in mid-air (future threat).
    """
    p_count = 0
    o_count = 0
    empty_idx = -1

    for i in range(4):
        c = cells[i]
        if c == player:
            p_count += 1
        elif c == opponent:
            o_count += 1
        else:
            empty_idx = i

    # Mixed windows — both players present, no one can complete this line
    if p_count > 0 and o_count > 0:
        return 0

    if p_count == 4:
        return FOUR_WEIGHT

    # 3-of-ours + 1 empty: check if the empty cell is immediately playable
    if p_count == 3:
        if empty_idx >= 0:
            row, col = cells[empty_idx + 4], cells[empty_idx + 8]
            if heights[col] == row:
                return THREE_IMMEDIATE
        return THREE_WEIGHT

    if p_count == 2:
        return TWO_WEIGHT

    # 3-of-opponent + 1 empty: checking if next 4-of is possible
    if o_count == 3:
        if empty_idx >= 0:
            row, col = cells[empty_idx + 4], cells[empty_idx + 8]
            if heights[col] == row:
                return OPP_THREE_IMMEDIATE
        return OPP_THREE_WEIGHT

    if o_count == 2:
        return OPP_TWO_WEIGHT

    return 0


def _score_center(board_arr: list[int], heights: list[int],
                  player: int, opponent: int) -> int:
    """Graduated positional bonus for pieces near the center of the board."""
    score = 0
    for col in range(COLS_RANGE):
        w = CENTER_WEIGHTS[col]
        if w == 0:
            continue
        for row in range(heights[col]):
            cell = board_arr[row * COLS_RANGE + col]
            if cell == player:
                score += w
            elif cell == opponent:
                score -= w
    return score


def _score_all_windows(board_arr: list[int], heights: list[int],
                       player: int, opponent: int) -> int:
    """Scan every possible 4-cell line on the board and sum their scores."""
    score = 0

    # cells layout: [val0, val1, val2, val3, row0, row1, row2, row3, col0, col1, col2, col3]

    # Horizontal windows
    for row in range(ROWS):
        base = row * COLS_RANGE
        for col in range(COLS_RANGE - 3):
            cells = [
                board_arr[base + col],     board_arr[base + col + 1],
                board_arr[base + col + 2], board_arr[base + col + 3],
                row, row, row, row,
                col, col + 1, col + 2, col + 3,
            ]
            score += _score_window(cells, player, opponent, heights)

    # Vertical windows
    for col in range(COLS_RANGE):
        for row in range(ROWS - 3):
            cells = [
                board_arr[row * COLS_RANGE + col],       board_arr[(row + 1) * COLS_RANGE + col],
                board_arr[(row + 2) * COLS_RANGE + col], board_arr[(row + 3) * COLS_RANGE + col],
                row, row + 1, row + 2, row + 3,
                col, col, col, col,
            ]
            score += _score_window(cells, player, opponent, heights)

    # Diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLS_RANGE - 3):
            cells = [
                board_arr[row * COLS_RANGE + col],             board_arr[(row + 1) * COLS_RANGE + col + 1],
                board_arr[(row + 2) * COLS_RANGE + col + 2],   board_arr[(row + 3) * COLS_RANGE + col + 3],
                row, row + 1, row + 2, row + 3,
                col, col + 1, col + 2, col + 3,
            ]
            score += _score_window(cells, player, opponent, heights)

    # Diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLS_RANGE - 3):
            cells = [
                board_arr[row * COLS_RANGE + col],             board_arr[(row - 1) * COLS_RANGE + col + 1],
                board_arr[(row - 2) * COLS_RANGE + col + 2],   board_arr[(row - 3) * COLS_RANGE + col + 3],
                row, row - 1, row - 2, row - 3,
                col, col + 1, col + 2, col + 3,
            ]
            score += _score_window(cells, player, opponent, heights)

    return score


def evaluate_board(board: Connect4Board, player: int) -> int:
    """
    Static evaluation of a Connect Four board position.

    Returns a positive score when the position favors `player`,
    negative when it favors the opponent, and near-zero for neutral positions.

    """
    opponent = PLAYER_1 if player == PLAYER_2 else PLAYER_2
    board_arr = board.board
    heights = board.heights

    return (_score_all_windows(board_arr, heights, player, opponent)
            + _score_center(board_arr, heights, player, opponent))