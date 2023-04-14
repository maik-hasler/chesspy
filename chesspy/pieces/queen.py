from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Queen(Piece):
    """Represents a queen piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Queen object.
        Args:
            color (Color): The color of the Queen.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a queen on the chess board.
        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position

        # Check if the move is diagonal
        if abs(end_row - start_row) == abs(end_col - start_col):
            # Check if the diagonal is blocked
            if Piece.is_diagonal_line_blocked(move, board):
                return False
            return True

        # Check if the move is horizontal or vertical
        if start_row == end_row:
            # Check if the horizontal line is blocked
            if Piece.is_horizontal_line_blocked(move, board):
                return False
            return True
        
        elif start_col == end_col:
            # Check if the vertical line is blocked
            if Piece.is_vertical_line_blocked(move, board):
                return False
            return True

        return False