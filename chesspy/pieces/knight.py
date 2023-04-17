from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Knight(Piece):
    """Represents a knight piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Knight object."""
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a knight on the chess board."""
        # Check if the move is within the knight's range of movement
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Check if the knight can capture a piece on the end position
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True
            # The knight can move to an empty square
            elif board[end_row][end_col] is None:
                return True
        return False
