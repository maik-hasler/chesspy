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
        # Check if the move is diagonal
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False

        # Check if there are any pieces in the way
        if start_row < end_row:
            row_step = 1
        else:
            row_step = -1
        if start_col < end_col:
            col_step = 1
        else:
            col_step = -1
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step

        # Check if the bishop can capture a piece on the end position
        if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True

        return True