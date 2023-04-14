from typing import Tuple

class Move:
    """Represents a chess move."""

    def __init__(self, start_position: Tuple[int, int], end_position: Tuple[int, int]) -> None:
        """Initializes a new Move object.

        Args:
            start_position (Tuple[int, int]): The starting position of the move as a tuple of two integers representing
                the row and column index of the square.
            end_position (Tuple[int, int]): The ending position of the move as a tuple of two integers representing
                the row and column index of the square.
        """
        self.start_position = start_position
        self.end_position = end_position

    @staticmethod
    def is_same_row(start_position: Tuple[int, int], end_position: Tuple[int, int]) -> bool:
        """Checks if the start and end positions are in the same row.

        Args:
            start_position (Tuple[int, int]): The starting position of the move.
            end_position (Tuple[int, int]): The ending position of the move.

        Returns:
            bool: True if the start and end positions are in the same row, False otherwise.
        """
        return start_position[0] == end_position[0]
    
    @staticmethod
    def is_same_column(start_position: Tuple[int, int], end_position: Tuple[int, int]) -> bool:
        """Checks if the start and end positions are in the same column.

        Args:
            start_position (Tuple[int, int]): The starting position of the move.
            end_position (Tuple[int, int]): The ending position of the move.

        Returns:
            bool: True if the start and end positions are in the same column, False otherwise.
        """
        return start_position[1] == end_position[1]
    
    @staticmethod
    def is_same_square(start_position: Tuple[int, int], end_position: Tuple[int, int]) -> bool:
        """Checks whether the start and end positions represent the same square.

        Args:
            start_position (Tuple[int, int]): The starting position of the move.
            end_position (Tuple[int, int]): The ending position of the move.

        Returns:
            bool: True if the start and end positions are the same, False otherwise.
        """
        return start_position == end_position
    
    @staticmethod
    def is_diagonal_move(start_position: Tuple[int, int], end_position: Tuple[int, int]) -> bool:
        """Checks whether a move is diagonal.

        Args:
            start_position (Tuple[int, int]): The starting position of the move.
            end_position (Tuple[int, int]): The ending position of the move.

        Returns:
            bool: True if the move is diagonal, False otherwise.
        """
        start_row, start_col = start_position
        end_row, end_col = end_position
        return abs(start_row - end_row) == abs(start_col - end_col)
    
    def __eq__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return self.start_position == other.start_position and self.end_position == other.end_position