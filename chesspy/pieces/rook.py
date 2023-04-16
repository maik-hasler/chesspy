from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Rook(Piece):
    """Represents a rook piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Rook object.
        Args:
            color (Color): The color of the Rook.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a rook on the chess board.
        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if Move.is_same_square(move.start_position, move.end_position):
            return False

        if not Move.is_same_row(move.start_position, move.end_position) and not Move.is_same_column(move.start_position, move.end_position):
            return False

        if move.start_position[0] == move.end_position[0]:
            if Piece.is_horizontal_line_blocked(move, board):
                return False

        if move.start_position[1] == move.end_position[1]:
            if Piece.is_vertical_line_blocked(move, board):
                return False

        return True
