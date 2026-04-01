ROWS = 6
COLS = 7
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

class Connect4Board:
    def __init__(self):
        self.board = [EMPTY] * (ROWS * COLS)
        self.heights = [0] * COLS
        self.move_history = []   # stores (column, player)
        self.last_move = None
        self.last_player = None
        self.total_moves = 0

    def index(self, row, col):
        return row * COLS + col

    def get_cell(self, row, col):
        return self.board[self.index(row, col)]

    def set_cell(self, row, col, value):
        self.board[self.index(row, col)] = value

    def apply_move(self, column, player):
        if column < 0 or column >= COLS:
            return False

        if player not in (PLAYER_1, PLAYER_2):
            return False

        if self.heights[column] >= ROWS:
            return False

        row = self.heights[column]
        self.set_cell(row, column, player)
        self.heights[column] += 1
        self.move_history.append((column, player))
        self.last_move = (row, column)
        self.last_player = player
        self.total_moves += 1
        return True

    def undo_move(self):
        if not self.move_history:
            return False

        column, player = self.move_history.pop()

        self.heights[column] -= 1
        row = self.heights[column]
        self.set_cell(row, column, EMPTY)
        self.total_moves -= 1

        if self.move_history:
            prev_col, prev_player = self.move_history[-1]
            prev_row = self.heights[prev_col] - 1
            self.last_move = (prev_row, prev_col)
            self.last_player = prev_player
        else:
            self.last_move = None
            self.last_player = None

        return True

    def get_legal_moves(self):
        preferred_order = [3, 2, 4, 1, 5, 0, 6]
        return [col for col in preferred_order if self.heights[col] < ROWS]

    def is_full(self):
        return self.total_moves == ROWS * COLS

    def is_terminal_state(self):
        if self.last_move is None:
            return False, None

        row, col = self.last_move
        player = self.last_player

        if self._check_win_from_position(row, col, player):
            return True, player

        if self.is_full():
            return True, 0

        return False, None

    def _check_win_from_position(self, row, col, player):
        directions = [
            (1, 0),   # vertical
            (0, 1),   # horizontal
            (1, 1),   # diagonal
            (1, -1),  # diagonal
        ]

        for dr, dc in directions:
            count = 1
            count += self._count_direction(row, col, dr, dc, player)
            count += self._count_direction(row, col, -dr, -dc, player)

            if count >= 4:
                return True

        return False

    def _count_direction(self, row, col, dr, dc, player):
        count = 0
        r, c = row + dr, col + dc

        while 0 <= r < ROWS and 0 <= c < COLS and self.get_cell(r, c) == player:
            count += 1
            r += dr
            c += dc

        return count

    def print_board(self):
        for row in range(ROWS - 1, -1, -1):
            print([self.get_cell(row, col) for col in range(COLS)])
        print()