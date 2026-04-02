from board_logic import Connect4Board, PLAYER_1, PLAYER_2, EMPTY
from heuristic_evaluator import evaluate_board

# ==============================================================================
# CONSTANTS
# ==============================================================================

WIN_SCORE  =  1_000_000
LOSS_SCORE = -1_000_000
DRAW_SCORE = 0


# ==============================================================================
# MINIMAX ALGORITHM
# ==============================================================================

def minimax(board: Connect4Board,
            depth: int,
            maximizing_player: bool,
            player: int,
            opponent: int) -> tuple[int, int | None]:
    """
    Recursive Minimax search algorithm.

    Explores the game tree up to `depth` levels deep, choosing the move
    that maximizes the AI's score (assuming the opponent plays optimally too).

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
        False → it is the opponent's turn (we want the lowest score).
    player : int
        The maximizing player's piece (PLAYER_1 or PLAYER_2).
    opponent : int
        The minimizing player's piece.

    Returns
    -------
    (score, best_column) : tuple[int, int | None]
        score       – the minimax value of the best reachable state.
        best_column – the column index that leads to that state,
                      or None at leaf nodes (terminal / depth == 0).
    """

    # BASE CASE 1: Terminal state (someone won, or the board is full)
    is_terminal, winner = board.is_terminal_state()
    if is_terminal:
        if winner == player:
            return WIN_SCORE + depth, None
        elif winner == opponent:
            return LOSS_SCORE - depth, None
        else:
            return DRAW_SCORE, None

    # BASE CASE 2: Depth limit reached — evaluate the board heuristically
    if depth == 0:
        score = evaluate_board(board, player)
        return score, None

    # RECURSIVE CASE
    legal_moves = board.get_legal_moves()

    if maximizing_player:
        best_score  = float('-inf')
        best_column = legal_moves[0]

        for col in legal_moves:
            board.apply_move(col, player)
            score, _ = minimax(board, depth - 1, False, player, opponent)
            board.undo_move()

            if score > best_score:
                best_score  = score
                best_column = col

        return best_score, best_column

    else:
        best_score  = float('inf')
        best_column = legal_moves[0]

        for col in legal_moves:
            board.apply_move(col, opponent)
            score, _ = minimax(board, depth - 1, True, player, opponent)
            board.undo_move()

            if score < best_score:
                best_score  = score
                best_column = col

        return best_score, best_column


# PUBLIC HELPER — called by main.py / simulation.py

def get_best_move(board: Connect4Board, depth: int = 5, player: int = PLAYER_2) -> int:
    """
    Convenience wrapper to ask for the AI's best column.

    Parameters
    ----------
    board  : Connect4Board — current game state (not modified).
    depth  : int — search depth (default 5).
    player : int — which player the AI is maximizing for (default PLAYER_2).

    Returns
    -------
    int — the column index the AI should play.
    """
    opponent = PLAYER_1 if player == PLAYER_2 else PLAYER_2
    _, best_col = minimax(board, depth, maximizing_player=True,
                          player=player, opponent=opponent)
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