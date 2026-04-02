from main import create_dummy_board

def test_board_creation():
    """Tests if the initial game board is created with the correct 7x6 dimensions."""
    board = create_dummy_board()
    
    # Check that there are 6 rows
    assert len(board) == 6
    
    # Check that there are 7 columns in the first row
    assert len(board[0]) == 7
    
    # Check that the board is completely empty (filled with 0s)
    assert board[0][0] == 0
    assert board[5][6] == 0