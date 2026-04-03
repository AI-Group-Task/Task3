import time
from board_logic import Connect4Board, PLAYER_1, PLAYER_2
from minimax_search import get_best_move as get_minimax_move
from alpha_beta_pruning import get_best_move as get_alphabeta_move

def run_match(p1_algo, p2_algo):
    print(f"\nStarting Match: {p1_algo} vs {p2_algo}")
    print("Depth limit set to 4 for both agents.")
    print("-" * 50)
    
    board = Connect4Board()
    game_over = False
    turn = 0 
    
    # --- Performance Trackers ---
    p1_time, p2_time = 0.0, 0.0
    p1_moves, p2_moves = 0, 0
    p1_pruned, p2_pruned = 0, 0
    
    while not game_over:
        current_player = PLAYER_1 if turn == 0 else PLAYER_2
        current_algo = p1_algo if current_player == PLAYER_1 else p2_algo
        
        print(f"\nCurrent Board:")
        board.print_board()
        print(f"Player {current_player} ({current_algo}) is thinking...")
        
        # Start the stopwatch!
        start_time = time.time()
        
        if current_algo == "Alpha-Beta":
            col, pruned_count = get_alphabeta_move(board, depth=4, player=current_player)
            # Stop stopwatch BEFORE sleeping!
            execution_time = time.time() - start_time
            
            if current_player == PLAYER_1:
                p1_time += execution_time
                p1_moves += 1
                p1_pruned += pruned_count
            else:
                p2_time += execution_time
                p2_moves += 1
                p2_pruned += pruned_count
                
            print(f"-> Player {current_player} plays column {col} | Time: {execution_time:.4f}s | Pruned: {pruned_count}")
            
        else: # Standard Minimax
            col = get_minimax_move(board, depth=4, player=current_player)
            # Stop stopwatch BEFORE sleeping!
            execution_time = time.time() - start_time
            
            if current_player == PLAYER_1:
                p1_time += execution_time
                p1_moves += 1
            else:
                p2_time += execution_time
                p2_moves += 1
                
            print(f"-> Player {current_player} plays column {col} | Time: {execution_time:.4f}s")
            
     # Sleep for a moment to let the user see the move before the next turn
        time.sleep(0.5)
            
        board.apply_move(col, current_player)
        
        # WIN CHECK
        is_terminal, winner = board.is_terminal_state()
        if is_terminal:
            print("\n" + "="*50)
            print(" FINAL SIMULATION BOARD:")
            board.print_board()
            
            if winner == PLAYER_1:
                print(f"Game Over! Player 1 ({p1_algo}) wins!")
            elif winner == PLAYER_2:
                print(f"Game Over! Player 2 ({p2_algo}) wins!")
            else:
                print("Game Over! It's a perfectly logical draw!")
            
            # --- FINAL STATISTICS ---
            print("\n" + "="*40)
            print(" FINAL PERFORMANCE STATISTICS")
            print("="*40)
            
            if p1_moves > 0:
                print(f"PLAYER 1 ({p1_algo}):")
                print(f"  - Total moves: {p1_moves}")
                print(f"  - Total match time: {p1_time:.4f} seconds")
                print(f"  - Average time per move: {(p1_time/p1_moves):.4f} seconds")
                if p1_algo == "Alpha-Beta":
                    print(f"  - Total branches pruned: {p1_pruned}")
            
            if p2_moves > 0:
                print(f"\nPLAYER 2 ({p2_algo}):")
                print(f"  - Total moves: {p2_moves}")
                print(f"  - Total match time: {p2_time:.4f} seconds")
                print(f"  - Average time per move: {(p2_time/p2_moves):.4f} seconds")
                if p2_algo == "Alpha-Beta":
                    print(f"  - Total branches pruned: {p2_pruned}")
            
            print("="*40)
            game_over = True
            break
            
        turn = (turn + 1) % 2