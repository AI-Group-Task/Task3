import time
from board_logic import Connect4Board, PLAYER_1, PLAYER_2

# Import BOTH AIs and alias them so their names don't clash
from minimax_search import get_best_move as get_minimax_move
from alpha_beta_pruning import get_best_move as get_alphabeta_move

def play_human_vs_ai():
    print("\n--- Starting Human vs AI Game ---")
    print("Which AI opponent would you like to face?")
    print("1. Standard Minimax")
    print("2. Alpha-Beta Pruning")
    
    choice = input("Select an option (1 or 2): ")
    use_pruning = (choice == '2')
    
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        print("\nCurrent Board:")
        board.print_board()
        
        # HUMAN TURN (Player 1)
        if turn == 0:
            try:
                col = int(input("Player 1, choose a column (0-6): "))
                if col < 0 or col > 6 or not board.apply_move(col, PLAYER_1):
                    print("Invalid or full column. Try again.")
                    continue
                print(f"You selected column {col}.")
            except ValueError:
                print("Please enter a valid number.")
                continue
                
        # AI TURN (Player 2)
        else:
            print("AI is thinking...")
            time.sleep(0.5)
            
            # Switchboard logic executes the chosen AI
            if use_pruning:
                col, pruned_count = get_alphabeta_move(board, depth=5)
                print(f"AI drops a piece in column {col}. (Pruned {pruned_count} branches!)")
            else:
                col = get_minimax_move(board, depth=5)
                print(f"AI drops a piece in column {col}.")
                
            board.apply_move(col, PLAYER_2)
            
        # WIN CHECK
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n========================================")
            print(" FINAL BOARD:")
            board.print_board()
            
            if winner == PLAYER_1:
                print("You win!")
            elif winner == PLAYER_2:
                print("AI wins!")
            else:
                print("It's a draw!")
                
            game_over = True
            break
            
        turn = (turn + 1) % 2
        
    input("\nPress Enter to return to the Main Menu...")