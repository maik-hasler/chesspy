from abc import ABC, abstractmethod

from chesspy.move import Move


class Piece(ABC):
    """Represents a chess piece."""

    @abstractmethod
    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid on the chess board.
        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        pass

    @staticmethod
    def is_horizontal_line_blocked(move: Move, board) -> bool:
        """Checks if the horizontal line between the start and end positions of a move is blocked by other pieces.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the horizontal line is blocked, False otherwise.
        """
        start_row, start_col = move.start_position
        _, end_col = move.end_position

        step = 1 if start_col < end_col else -1
        for col in range(start_col + step, end_col, step):
            if board[start_row][col] is not None:
                return True  # There is a piece on the horizontal line

        if Piece.is_capture(move, board):
            return False

        # Check the end square, but only if it is not empty
        if board[start_row][end_col] is not None:
            return True

        return False  # The horizontal line is not blocked

    @staticmethod
    def is_vertical_line_blocked(move: Move, board) -> bool:
        """Checks if the vertical line between the start and end positions of a move is blocked by other pieces.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the vertical line is blocked, False otherwise.
        """
        start_row, _ = move.start_position
        end_row, _ = move.end_position
        col = move.start_position[1]

        if start_row < end_row:
            for row in range(start_row + 1, end_row):
                if board[row][col] is not None:
                    return True
        else:
            for row in range(end_row + 1, start_row):
                if board[row][col] is not None:
                    return True

        if Piece.is_capture(move, board):
            return False

        # Check the end square, but only if it is not empty
        if board[end_row][col] is not None:
            return True

        return False

    @staticmethod
    def is_diagonal_line_blocked(move: Move, board) -> bool:
        """Checks if the diagonal line between the start and end positions of a move is blocked by other pieces.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the diagonal line is blocked, False otherwise.
        """
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position

        if abs(start_row - end_row) != abs(start_col - end_col):
            return False  # The move is not diagonal

        step_row = 1 if start_row < end_row else -1
        step_col = 1 if start_col < end_col else -1

        row, col = start_row + step_row, start_col + step_col
        while row != end_row:
            if board[row][col] is not None:
                return True  # There is a piece on the diagonal line
            row += step_row
            col += step_col

        if Piece.is_capture(move, board):
            return False

        # Check if the end position is blocked
        if board[end_row][end_col] is not None:
            return True

        return False  # The diagonal line is not blocked

    @staticmethod
    def is_capture(move: Move, board) -> bool:
        """Checks whether the move is a capture move."""
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        piece = board[start_row][start_col]
        end_piece = board[end_row][end_col]
        if end_piece is None:
            return False
        return end_piece.color != piece.color