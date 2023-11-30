import unittest
from board import Board
from player import Player
from game import Game

class TestTicTacToe(unittest.TestCase):

    def test_initial_board_empty(self):
        board = Board()
        for row in board.board:
            for cell in row:
                self.assertIsNone(cell)

    def test_game_initialization(self):
        player1 = Player('X')
        player2 = Player('O')
        game = Game([player1, player2])
        self.assertEqual(len(game.players), 2)
        self.assertIsInstance(game.players[0], Player)
        self.assertIsInstance(game.players[1], Player)

    def test_players_have_unique_pieces(self):
        player1 = Player('X')
        player2 = Player('O')
        self.assertNotEqual(player1.symbol, player2.symbol)

    def test_alternate_turns(self):
        pass

    def test_detect_win_conditions(self):
        pass

    def test_only_play_in_empty_cells(self):
        board = Board()
        board.make_move(0, 0, 'X')
        self.assertFalse(board.make_move(0, 0, 'O'))

    def test_detect_winner(self): 
        pass

if __name__ == '__main__':
    unittest.main()


