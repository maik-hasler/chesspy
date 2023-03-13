from enum import Enum

class Piece():
    
    def __init__(self, color, type):
        self.color = color
        self.type = type

class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class ColorType(Enum):
    WHITE = 1
    BLACK = 2