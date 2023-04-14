import unittest
from chesspy.piece import Pawn, Color
from chesspy.move import Move
from chesspy.board import Board

class PieceTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_pawn = self.board.board[1][0]

    def test_is_valid_move(self):
        move = Move((1, 0), (2, 0))
        self.assertTrue(self.white_pawn.is_valid_move(move, self.board.board))

if __name__ == '__main__':
    unittest.main()