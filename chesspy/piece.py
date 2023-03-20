from enum import Enum

class Piece():
    
    def __init__(self, color, type, path_to_image):
        self.color = color
        self.type = type
        self.path_to_image = path_to_image

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