class Board:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join([' ' if cell is None else cell for cell in row]))
            print("-" * 9)

    def make_move(self, row, col, player):
        if self.board[row][col] is None:
            self.board[row][col] = player
            return True
        else:
            print("Invalid move! Cell already taken.")
            return False

    def get_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_full(self):
        return all(cell is not None for row in self.board for cell in row)