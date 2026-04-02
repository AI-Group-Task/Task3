import time
from board_logic import Connect4Board, PLAYER_1, PLAYER_2

# Imported BOTH AIs and alias them so their names don't clash
from minimax_search import get_best_move as get_minimax_move
from alpha_beta_pruning import get_best_move as get_alphabeta_move

def run_ai_simulation():
    print("\n--- Starting AI vs AI Simulation ---")
    print("Which algorithm should the AI use?")
    print("1. Standard Minimax (Slow)")
    print("2. Alpha-Beta Pruning (Fast)")
    
    choice = input("Select an option (1 or 2): ")
    use_pruning = (choice == '2')
    
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        current_player = PLAYER_1 if turn == 0 else PLAYER_2
        print(f"\nCurrent Board (AI 1 vs AI 2):")
        board.print_board()
        
        print(f"AI {current_player} is thinking...")
        time.sleep(0.5) 
        
        if use_pruning:
            col, pruned_count = get_alphabeta_move(board, depth=4, player=current_player)
            print(f"AI {current_player} plays column {col} | Nodes Pruned: {pruned_count}")
        else:
            col = get_minimax_move(board, depth=4, player=current_player)
            print(f"AI {current_player} plays column {col}")
            
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