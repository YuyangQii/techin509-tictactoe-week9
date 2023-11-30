import random

class Player:
    def __init__(self, symbol, is_bot=False):
        self.symbol = symbol
        self.is_bot = is_bot

    def make_move(self, board):
        if self.is_bot:
            return self.make_bot_move(board)
        else:
            return self.make_human_move()

    def make_bot_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_cells) if empty_cells else None

    def make_human_move(self):
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        return row, col







