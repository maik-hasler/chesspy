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
        # Check if the move is a valid rook move
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        if start_row != end_row and start_col != end_col:
            return False

        # Check if there are any pieces in the way of the move
        if start_row == end_row:
            # Horizontal move
            start_col, end_col = sorted([start_col, end_col])
            for col in range(start_col+1, end_col):
                if board[start_row][col] is not None:
                    return False
        else:
            # Vertical move
            start_row, end_row = sorted([start_row, end_row])
            for row in range(start_row+1, end_row):
                if board[row][start_col] is not None:
                    return False

        # Check if the rook can capture a piece on the end position
        if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True

        return True