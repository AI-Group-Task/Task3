from board_logic import Connect4Board

def test_initial_legal_moves():
    """Tests that a fresh board has all 7 columns available."""
    board = Connect4Board()
    legal_moves = board.get_legal_moves()
    
    # A brand new board should have exactly 7 legal moves
    assert len(legal_moves) == 7
    
    # Optional: Verify it returns columns 0 through 6
    for i in range(7):
        assert i in legal_moves

def test_apply_move():
    """Tests if applying a move works and does not trigger a false win."""
    board = Connect4Board()
    
    # Player 1 drops a piece in column 3
    success = board.apply_move(3, 1)
    assert success == True
    
    # The game should definitely not be over after one move
    is_terminal, winner = board.is_terminal_state()
    assert is_terminal == False
    assert winner == None

def test_full_column():
    """Tests that a full column rejects new pieces and is removed from legal moves."""
    board = Connect4Board()
    
    # Fill up column 2 with 6 pieces
    for _ in range(6):
        board.apply_move(2, 1)
        
    legal_moves = board.get_legal_moves()
    
    # Column 2 should no longer exist in the legal moves list
    assert 2 not in legal_moves
    
    # Attempting to drop a 7th piece should return False
    assert board.apply_move(2, 1) == False


def test_vertical_win():
    """Tests if the engine correctly detects a 4-in-a-row vertical win."""
    board = Connect4Board()
    
    # Player 1 drops 4 pieces in column 0
    board.apply_move(0, 1)
    board.apply_move(0, 1)
    board.apply_move(0, 1)
    board.apply_move(0, 1)
    
    is_terminal, winner = board.is_terminal_state()
    
    assert is_terminal == True
    assert winner == 1


def test_horizontal_win():
    """Tests if the engine correctly detects a 4-in-a-row horizontal win."""
    board = Connect4Board()
    
    # Player 2 drops pieces in the bottom row of columns 2, 3, 4, and 5
    board.apply_move(2, 2)
    board.apply_move(3, 2)
    board.apply_move(4, 2)
    board.apply_move(5, 2)
    
    is_terminal, winner = board.is_terminal_state()
    
    assert is_terminal == True
    assert winner == 2

def test_positive_diagonal_win():
    """Tests if the engine correctly detects a 4-in-a-row diagonal win (up-right)."""
    board = Connect4Board()
    
    # Column 0: 1 piece (Player 1)
    board.apply_move(0, 1)
    
    # Column 1: 2 pieces (Player 2, then Player 1)
    board.apply_move(1, 2)
    board.apply_move(1, 1)
    
    # Column 2: 3 pieces (Player 1, Player 2, then Player 1)
    board.apply_move(2, 1)
    board.apply_move(2, 2)
    board.apply_move(2, 1)
    
    # Column 3: 4 pieces (Player 2, Player 1, Player 2, then Player 1)
    board.apply_move(3, 2)
    board.apply_move(3, 1)
    board.apply_move(3, 2)
    board.apply_move(3, 1)
    
    is_terminal, winner = board.is_terminal_state()
    
    assert is_terminal == True
    assert winner == 1


def test_negative_diagonal_win():
    """Tests if the engine correctly detects a 4-in-a-row diagonal win (down-right)."""
    board = Connect4Board()
    
    # Column 3: 1 piece (Player 2)
    board.apply_move(3, 2)
    
    # Column 2: 2 pieces (Player 1, then Player 2)
    board.apply_move(2, 1)
    board.apply_move(2, 2)
    
    # Column 1: 3 pieces (Player 1, Player 1, then Player 2)
    board.apply_move(1, 1)
    board.apply_move(1, 1)
    board.apply_move(1, 2)
    
    # Column 0: 4 pieces (Player 1, Player 2, Player 1, then Player 2)
    board.apply_move(0, 1)
    board.apply_move(0, 2)
    board.apply_move(0, 1)
    board.apply_move(0, 2)
    
    is_terminal, winner = board.is_terminal_state()
    
    assert is_terminal == True
    assert winner == 2
