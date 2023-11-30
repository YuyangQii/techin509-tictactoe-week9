import os
import csv
import logging
from board import Board
from player import Player

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.game_moves = []  # To track moves and stats for CSV
        self.setup_logging()

    def start(self):
        logging.info("Game started")
        while self.board.get_winner() is None and not self.board.is_full():
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            row, col = current_player.make_move(self.board.board)
            if self.board.make_move(row, col, current_player.symbol):
                self.log_move(current_player, row, col)
                self.game_moves.append([current_player.symbol, row, col])
                self.switch_player()
            else:
                logging.warning(f"Invalid move by {current_player.symbol}")
        self.end_game()
        self.save_game_results_to_csv()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def end_game(self):
        self.board.print_board()
        winner = self.board.get_winner()
        if winner:
            print(f"\\n{winner} wins!")
            logging.info(f"{winner} wins!")
            self.game_moves.append(['Winner', winner])
        else:
            print("\\nThe game is a draw.")
            logging.info("The game is a draw.")
            self.game_moves.append(['Draw'])

    def log_move(self, player, row, col):
        logging.info(f'Player {player.symbol} moved to ({row}, {col})')

    def save_game_results_to_csv(self):
        csv_file = 'game_results.csv'
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            for move in self.game_moves:
                writer.writerow(move)

    @staticmethod
    def setup_logging():
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logging.basicConfig(
            filename=os.path.join(log_directory, 'game.log'),
            level=logging.INFO,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

if __name__ == '__main__':
    single_player_mode = input("Single player mode? (y/n): ").lower() == 'y'
    player1 = Player('X')
    if single_player_mode:
        player2 = Player('O', is_bot=True)
    else:
        player2 = Player('O')
    game = Game([player1, player2])
    game.start()
