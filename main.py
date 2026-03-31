import random
import time

# ==========================================
# DUMMY FUNCTIONS (To be replaced later)
# ==========================================

def create_dummy_board():
    """Creates a blank 7x6 board using 0s for empty spaces."""
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board):
    """Prints the board to the terminal."""
    print("\n  0 1 2 3 4 5 6")
    print(" ---------------")
    for row in board:
        # Replaces 0 with '.', 1 with 'X', 2 with 'O' for readability
        row_str = " ".join(['.' if c == 0 else 'X' if c == 1 else 'O' for c in row])
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
    
    board = create_dummy_board()
    game_over = False
    turn = 0 # 0 for Human (Player 1), 1 for AI (Player 2)
    
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
                
                print(f"You selected column {col}.")
                # TODO: Call Kevin's apply_move(board, col, player=1) here
                
            except ValueError:
                print("Please enter a valid number.")
                continue
                
        # ----------------------
        # AI TURN
        # ----------------------
        else:
            print("AI (O) is thinking...")
            time.sleep(1) # Fake thinking time
            
            # TODO: Call the Minimax function here to get the best column
            # Example: col, score = minimax(board, depth=5, alpha, beta, True)
            col = random.randint(0, 6) # Dummy random move
            
            print(f"AI drops a piece in column {col}.")
            # TODO: Call Kevin's apply_move(board, col, player=2) here
        
        # Check for a win (Will use Kevin's is_terminal_state() later)
        if check_win_dummy(board):
            print_board(board)
            winner = "Player 1" if turn == 0 else "AI"
            print(f"Game Over! {winner} wins!")
            game_over = True
            
        # Switch turns
        turn = (turn + 1) % 2
        
        # Temporary breakout so the dummy loop doesn't run forever during testing
        if input("Continue testing? (y/n): ").lower() == 'n':
            print("Testing ended by user.")
            break

if __name__ == "__main__":
    main()