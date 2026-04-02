import random
import time
from board_logic import Connect4Board

def play_human_vs_ai():
    print("\n--- Starting Human vs AI Game ---")
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        print("\nCurrent Board (0=Empty, 1=Human, 2=AI):")
        board.print_board()
        
        # HUMAN TURN
        if turn == 0:
            try:
                col = int(input("Player 1, choose a column (0-6): "))
                if col < 0 or col > 6 or not board.apply_move(col, 1):
                    print("Invalid or full column. Try again.")
                    continue
                print(f"You selected column {col}.")
            except ValueError:
                print("Please enter a valid number.")
                continue
                
        # AI TURN
        else:
            print("AI (2) is thinking...")
            time.sleep(1)
            
            legal_moves = board.get_legal_moves()
            if not legal_moves: break
            col = random.choice(legal_moves)
            
            print(f"AI drops a piece in column {col}.")
            board.apply_move(col, 2)
        
        # WIN CHECK
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n========================================")
            print(" FINAL BOARD:")
            board.print_board()
            if winner == 1: 
                print("You win!")
            elif winner == 2: 
                print("AI wins!")
            else: 
                print("It's a draw!")
            game_over = True
            break
            
        turn = (turn + 1) % 2
        
    input("\nPress Enter to return to the Main Menu...")