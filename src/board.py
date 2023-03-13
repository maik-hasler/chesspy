from piece import Piece, ColorType, PieceType

class Board():
    
    def create():
        board = [
            Piece(ColorType.BLACK, PieceType.ROOK, '../assets/Black-Rook.png'),
            Piece(ColorType.BLACK, PieceType.KNIGHT, ''),
            Piece(ColorType.BLACK, PieceType.BISHOP, ''),
            Piece(ColorType.BLACK, PieceType.QUEEN, ''),
            Piece(ColorType.BLACK, PieceType.KING, ''),
            Piece(ColorType.BLACK, PieceType.BISHOP, ''),
            Piece(ColorType.BLACK, PieceType.KNIGHT, ''),
            Piece(ColorType.BLACK, PieceType.ROOK, '../assets/Black-Rook.png'),

            Piece(ColorType.BLACK, PieceType.PAWN, '../assets/Black-Rook.png'),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, ''),
            Piece(ColorType.BLACK, PieceType.PAWN, '../assets/Black-Rook.png'),

            # How to do the four empty rows?

            Piece(ColorType.WHITE, PieceType.PAWN, '../assets/Black-Rook.png'),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, ''),
            Piece(ColorType.WHITE, PieceType.PAWN, '../assets/Black-Rook.png'),

            Piece(ColorType.WHITE, PieceType.ROOK, '../assets/Black-Rook.png'),
            Piece(ColorType.WHITE, PieceType.KNIGHT, ''),
            Piece(ColorType.WHITE, PieceType.BISHOP, ''),
            Piece(ColorType.WHITE, PieceType.QUEEN, ''),
            Piece(ColorType.WHITE, PieceType.KING, ''),
            Piece(ColorType.WHITE, PieceType.BISHOP, ''),
            Piece(ColorType.WHITE, PieceType.KNIGHT, ''),
            Piece(ColorType.WHITE, PieceType.ROOK, '../assets/Black-Rook.png')
        ]