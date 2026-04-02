import time
from board_logic import Connect4Board, PLAYER_1, PLAYER_2
from minimax_search import get_best_move

def run_ai_simulation():
    print("\n--- Starting AI vs AI Simulation ---")
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        current_player = PLAYER_1 if turn == 0 else PLAYER_2
        print(f"\nCurrent Board (AI 1 vs AI 2):")
        board.print_board()
        
        print(f"AI {current_player} is thinking...")
        time.sleep(0.5)
        
        # Both players use the Minimax algorithm here
        col = get_best_move(board, depth=4)
        
        print(f"AI {current_player} drops a piece in column {col}.")
        board.apply_move(col, current_player)
        
        # WIN CHECK
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n========================================")
            print(" FINAL SIMULATION BOARD:")
            board.print_board()
            
            if winner == PLAYER_1:
                print("Game Over! AI 1 wins!")
            elif winner == PLAYER_2:
                print("Game Over! AI 2 wins!")
            else:
                print("Game Over! It's a draw!")
            
            game_over = True
            break
            
        turn = (turn + 1) % 2
        
    input("\nPress Enter to return to the Main Menu...")