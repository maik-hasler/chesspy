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