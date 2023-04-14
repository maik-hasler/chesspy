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
            # Check if there are pieces in the way of the diagonal move
            if end_row > start_row and end_col > start_col:
                for i in range(1, end_row - start_row):
                    if board[start_row+i][start_col+i] is not None:
                        return False
            elif end_row > start_row and end_col < start_col:
                for i in range(1, end_row - start_row):
                    if board[start_row+i][start_col-i] is not None:
                        return False
            elif end_row < start_row and end_col > start_col:
                for i in range(1, start_row - end_row):
                    if board[start_row-i][start_col+i] is not None:
                        return False
            else:
                for i in range(1, start_row - end_row):
                    if board[start_row-i][start_col-i] is not None:
                        return False
            return True

        # Check if the move is horizontal or vertical
        if start_row == end_row:
            # Check if there are pieces in the way of the horizontal move
            if end_col > start_col:
                for i in range(start_col+1, end_col):
                    if board[start_row][i] is not None:
                        return False
            else:
                for i in range(end_col+1, start_col):
                    if board[start_row][i] is not None:
                        return False
            return True
        elif start_col == end_col:
            # Check if there are pieces in the way of the vertical move
            if end_row > start_row:
                for i in range(start_row+1, end_row):
                    if board[i][start_col] is not None:
                        return False
            else:
                for i in range(end_row+1, start_row):
                    if board[i][start_col] is not None:
                        return False
            return True

        return False