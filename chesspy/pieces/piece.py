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
