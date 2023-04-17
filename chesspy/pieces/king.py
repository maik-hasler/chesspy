from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class King(Piece):
    """Represents a king piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new King object."""
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a king on the chess board."""
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position

        # Check if the move is within the King's range of movement
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if row_diff <= 1 and col_diff <= 1:
            # Check if there are any pieces blocking the King's way
            if board[end_row][end_col] is not None and board[end_row][end_col].color == self.color:
                return False
            if row_diff == 0 and col_diff == 0:
                return False
            return True

        return False
