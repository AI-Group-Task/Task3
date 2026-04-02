from board_logic import Connect4Board, PLAYER_1, PLAYER_2, EMPTY
from heuristic_evaluator import evaluate_board

# ==============================================================================
# CONSTANTS
# ==============================================================================

AI_PLAYER    = PLAYER_2   
HUMAN_PLAYER = PLAYER_1  

WIN_SCORE  =  1_000_000
LOSS_SCORE = -1_000_000
DRAW_SCORE = 0


# ==============================================================================
# PLACEHOLDER HEURISTIC
# Replace this entire function once Role 4 (heuristic_evaluator.py) is ready.
# Expected signature: evaluate_board(board: Connect4Board, player: int) -> int/float
# ==============================================================================

def _placeholder_evaluate(board: Connect4Board, player: int) -> int:
    """
    Temporary static evaluation function.
    Awards a small bonus for occupying the center column (column 3),
    which is a well-known positional advantage in Connect Four.

    TODO: Replace with Role 4's evaluate_board() once available.
          Import it like:
              from heuristic_evaluator import evaluate_board
          Then call:
              evaluate_board(board, AI_PLAYER)
    """
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
    """
    Recursive Minimax search algorithm.

    Explores the game tree up to `depth` levels deep, choosing the move
    that maximizes the AI's score (assuming the human plays optimally too).

    Parameters
    ----------
    board : Connect4Board
        The current game state. Moves are applied and undone in-place,
        so the same board object is reused throughout the entire search.
    depth : int
        How many more plies (half-moves) to search before falling back
        to the heuristic evaluation. A depth of 0 means "evaluate now."
    maximizing_player : bool
        True  → it is the AI's turn  (we want the highest score).
        False → it is the human's turn (we want the lowest score).

    Returns
    -------
    (score, best_column) : tuple[int, int | None]
        score       – the minimax value of the best reachable state.
        best_column – the column index that leads to that state,
                      or None at leaf nodes (terminal / depth == 0).

    How the search works
    --------------------
    1. Check if the current state is terminal (win/draw) or depth is 0.
       If so, return a score immediately — this is the base case.

    2. Otherwise, iterate over every legal column (Kevin's get_legal_moves()
       already orders them center-first for a slight speed benefit).

    3. For each column:
       a. Apply the move (board.apply_move).
       b. Recurse one level deeper with the opponent's perspective.
       c. Undo the move (board.undo_move) to restore the board.
       d. Track whether this move produced the best score so far.

    4. Return the best (score, column) pair found.
    """

    # BASE CASE 1: Terminal state (someone won, or the board is full)
    is_terminal, winner = board.is_terminal_state()
    if is_terminal:
        if winner == AI_PLAYER:
            return WIN_SCORE + depth, None
        elif winner == HUMAN_PLAYER:
            return LOSS_SCORE - depth, None
        else:
            return DRAW_SCORE, None

    # BASE CASE 2: Depth limit reached — evaluate the board heuristically
    if depth == 0:
        score = evaluate_board(board, AI_PLAYER)
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


# PUBLIC HELPER — called by main.py

def get_best_move(board: Connect4Board, depth: int = 5) -> int:
    """
    Convenience wrapper used by main.py to ask for the AI's best column.

    Parameters
    ----------
    board : Connect4Board
        Current game state (not modified).
    depth : int
        Search depth. 5 is a reasonable default; increase for stronger play
        (but slower). Role 5 will benchmark the right value empirically.

    Returns
    -------
    int
        The column index the AI should play.

    Usage in main.py
    ----------------
        from minimax_search import get_best_move
        col = get_best_move(board, depth=5)
        board.apply_move(col, PLAYER_2)
    """
    _, best_col = minimax(board, depth, maximizing_player=True)
    return best_col


# QUICK SMOKE TEST

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