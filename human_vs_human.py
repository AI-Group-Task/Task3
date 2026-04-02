from board_logic import Connect4Board

def play_human_vs_human():
    print("\n--- Starting Human vs Human Game ---")
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    while not game_over:
        player_num = turn + 1
        print(f"\nCurrent Board (0=Empty, 1=Player 1, 2=Player 2):")
        board.print_board()
        
        try:
            col = int(input(f"Player {player_num}, choose a column (0-6): "))
            if col < 0 or col > 6 or not board.apply_move(col, player_num):
                print("Invalid or full column. Try again.")
                continue
            print(f"Player {player_num} selected column {col}.")
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # WIN CHECK
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n========================================")
            print(" FINAL BOARD:")
            board.print_board()
            if winner == 1: 
                print("Player 1 wins!")
            elif winner == 2: 
                print("Player 2 wins!")
            else: 
                print("It's a draw!")
            game_over = True
            break
            
        turn = (turn + 1) % 2
        
    input("\nPress Enter to return to the Main Menu...")