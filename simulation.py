import random
import time
from board_logic import Connect4Board

def run_ai_simulation():
    print("\n--- Starting AI vs AI Simulation ---")
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        player_num = turn + 1
        print(f"\nCurrent Board (0=Empty, 1=AI 1, 2=AI 2):")
        board.print_board()
        
        print(f"AI {player_num} is thinking...")
        time.sleep(0.5) 
        
        # Temporary AI logic
        legal_moves = board.get_legal_moves()
        if not legal_moves:
            break
            
        col = random.choice(legal_moves)
        print(f"AI {player_num} drops a piece in column {col}.")
        board.apply_move(col, player_num)
        
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n========================================")
            print(" FINAL SIMULATION BOARD:")
            board.print_board()
            
            if winner == 1:
                print("Game Over! AI 1 wins!")
            elif winner == 2:
                print("Game Over! AI 2 wins!")
            else:
                print("Game Over! It's a draw!")
            
            game_over = True
            break
            
        turn = (turn + 1) % 2
        
    input("\nPress Enter to return to the Main Menu...")