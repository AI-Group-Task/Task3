from board_logic import Connect4Board, PLAYER_1, PLAYER_2, EMPTY

# ==============================================================================
# CONSTANTS
# ==============================================================================

AI_PLAYER    = PLAYER_2   
HUMAN_PLAYER = PLAYER_1  

WIN_SCORE  =  1_000_000
LOSS_SCORE = -1_000_000
DRAW_SCORE = 0


# ==============================================================================
# PERFORMANCE TRACKING
# ==============================================================================

nodes_expanded = 0


# ==============================================================================
# PLACEHOLDER HEURISTIC
# ==============================================================================

def _placeholder_evaluate(board: Connect4Board, player: int) -> int:
    score = 0
    CENTER_COL = 3
    from board_logic import ROWS

    for row in range(ROWS):
        if board.get_cell(row, CENTER_COL) == AI_PLAYER:
            score += 3
        elif board.get_cell(row, CENTER_COL) == HUMAN_PLAYER:
            score -= 3

    return score if player == AI_PLAYER else -score


# ==============================================================================
# MINIMAX ALGORITHM
# ==============================================================================

def minimax(board: Connect4Board,
            depth: int,
            maximizing_player: bool) -> tuple[int, int | None]:

    global nodes_expanded
    nodes_expanded += 1

    # BASE CASE 1: Terminal state
    is_terminal, winner = board.is_terminal_state()
    if is_terminal:
        if winner == AI_PLAYER:
            return WIN_SCORE + depth, None
        elif winner == HUMAN_PLAYER:
            return LOSS_SCORE - depth, None
        else:
            return DRAW_SCORE, None

    # BASE CASE 2: Depth limit reached
    if depth == 0:
        score = _placeholder_evaluate(board, AI_PLAYER)
        return score, None

    # RECURSIVE CASE
    legal_moves = board.get_legal_moves()

    if maximizing_player:
        best_score  = float('-inf')
        best_column = legal_moves[0]

        for col in legal_moves:
            board.apply_move(col, AI_PLAYER)
            score, _ = minimax(board, depth - 1, False)
            board.undo_move()

            if score > best_score:
                best_score  = score
                best_column = col

        return best_score, best_column

    else:
        best_score  = float('inf')
        best_column = legal_moves[0]

        for col in legal_moves:
            board.apply_move(col, HUMAN_PLAYER)
            score, _ = minimax(board, depth - 1, True)
            board.undo_move()

            if score < best_score:
                best_score  = score
                best_column = col

        return best_score, best_column


# ==============================================================================
# PUBLIC HELPER
# ==============================================================================

def get_best_move(board: Connect4Board, depth: int = 5) -> int:

    global nodes_expanded
    nodes_expanded = 0

    _, best_col = minimax(board, depth, maximizing_player=True)

    print(f"Nodes expanded: {nodes_expanded}")

    return best_col


# ==============================================================================
# QUICK TEST
# ==============================================================================

if __name__ == "__main__":
    print("--- Minimax Smoke Test ---\n")

    b = Connect4Board()

    b.apply_move(3, PLAYER_1)
    b.apply_move(3, PLAYER_2)
    b.apply_move(2, PLAYER_1)
    b.apply_move(4, PLAYER_2)

    b.print_board()

    best = get_best_move(b, depth=4)
    print(f"Minimax recommends column: {best}")