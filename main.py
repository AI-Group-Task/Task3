import random
import time
from board_logic import Connect4Board, PLAYER_1, PLAYER_2
from minimax_search import get_best_move

# ==========================================
# DUMMY FUNCTIONS (To be replaced later)
# ==========================================

def create_dummy_board():
    """Creates a blank 7x6 board using 0s for empty spaces."""
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board: Connect4Board):
    """Prints the board to the terminal using Kevin's board object."""
    from board_logic import ROWS, COLS
    print("\n  0 1 2 3 4 5 6")
    print(" ---------------")
    for row in range(ROWS - 1, -1, -1): 
        row_str = " ".join(
            ['.' if board.get_cell(row, col) == 0
             else 'X' if board.get_cell(row, col) == PLAYER_1
             else 'O'
             for col in range(COLS)]
        )
        print(f"| {row_str} |")
    print(" ---------------\n")

def check_win_dummy(board):
    """Dummy win checker. Always returns False for now."""
    return False

# ==========================================
# MAIN GAME LOOP
# ==========================================

def main():
    print("========================================")
    print(" Task 3: Connect Four AI (CLI Prototype)")
    print("========================================")

    board = Connect4Board() 
    game_over = False
    turn = 0  

    while not game_over:
        print_board(board)

        # ----------------------
        # HUMAN TURN
        # ----------------------
        if turn == 0:
            try:
                col = int(input("Player 1 (X), choose a column (0-6): "))
                if col < 0 or col > 6:
                    print("Invalid column. Please choose between 0 and 6.")
                    continue

                if not board.apply_move(col, PLAYER_1): 
                    print("Column is full. Choose another.")
                    continue

                print(f"You placed in column {col}.")

            except ValueError:
                print("Please enter a valid number.")
                continue

        # ----------------------
        # AI TURN
        # ----------------------
        else:
            print("AI (O) is thinking...")
            time.sleep(1)

            col = get_best_move(board, depth=5) 
            board.apply_move(col, PLAYER_2)
            print(f"AI drops a piece in column {col}.")

        # ----------------------
        # WIN / DRAW CHECK
        # ----------------------
        is_terminal, winner = board.is_terminal_state()   
        if is_terminal:
            print_board(board)
            if winner == PLAYER_1:
                print("Game Over! Player 1 (X) wins!")
            elif winner == PLAYER_2:
                print("Game Over! AI (O) wins!")
            else:
                print("Game Over! It's a draw!")
            game_over = True

        turn = (turn + 1) % 2

if __name__ == "__main__":
    main()