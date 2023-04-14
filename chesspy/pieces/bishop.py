from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Bishop(Piece):
    """Represents a bishop piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Bishop object.
        Args:
            color (Color): The color of the Bishop.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a bishop on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not Move.is_diagonal_move(move.start_position, move.end_position):
            return False

        if Piece.is_diagonal_line_blocked(move, board):
            return False

        return True