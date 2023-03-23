from enum import Enum
from chesspy.move import Move

class PieceType(Enum):
    """Enumeration representing the different types of chess pieces."""

    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Color(Enum):
    """Enumeration representing the two colors of chess pieces."""

    WHITE = 1
    BLACK = 2

class Piece:
    """Represents a chess piece."""

    def __init__(self, piece_type: PieceType, color: Color) -> None:
        """Initializes a new Piece object.

        Args:
            piece_type (PieceType): The type of the piece.
            color (Color): The color of the piece.
        """
        self.piece_type = piece_type
        self.color = color

    def is_valid_move(self, move: Move) -> bool:
        return True