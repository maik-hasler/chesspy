from copy import deepcopy
from typing import List, Tuple
from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.king import King
from chesspy.pieces.piece import Piece


def get_king_position(color: Color, board: List[List[Piece]]) -> Tuple[int, int]:
    """Gets the king position of the specified color"""
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == None or piece.color != color or not isinstance(piece, King):
                continue
            return (row, col)

def is_king_in_check(color: Color, board: List[List[Piece]]) -> bool:
    """Checks if the king of the specified color is in check."""
    king_pos = get_king_position(color)
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is None or piece.color == color or piece.is_valid_move(Move((row, col)), king_pos, board) == False:
                continue
            return True

def is_player_in_check_after_move(color: Color, move: Move, board: List[List[Piece]]) -> bool:
    """Checks if the player is in check after making a certain move."""
    test_board = deepcopy(board)
    start_pos = move.start_position
    end_pos = move.end_position
    test_board[end_pos[0]][end_pos[1]] = test_board[start_pos[0]][start_pos[1]]
    test_board[start_pos[0]][start_pos[1]] = None
    return is_king_in_check(color, test_board)
