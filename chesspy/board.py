from chesspy.piece import Piece, PieceType, Color
from chesspy.move import Move

class Board:
    """Represents a chess board."""

    def __init__(self):
        self.game_over = False
        self.board = self._init_board()
        self.current_player_index = 0

    def _init_board(self):
        return [
            [Piece(PieceType.ROOK, Color.WHITE), Piece(PieceType.KNIGHT, Color.WHITE), Piece(PieceType.BISHOP, Color.WHITE),
             Piece(PieceType.QUEEN, Color.WHITE), Piece(PieceType.KING, Color.WHITE), Piece(PieceType.BISHOP, Color.WHITE),
             Piece(PieceType.KNIGHT, Color.WHITE), Piece(PieceType.ROOK, Color.WHITE)],
            [Piece(PieceType.PAWN, Color.WHITE) for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Piece(PieceType.PAWN, Color.BLACK) for _ in range(8)],
            [Piece(PieceType.ROOK, Color.BLACK), Piece(PieceType.KNIGHT, Color.BLACK), Piece(PieceType.BISHOP, Color.BLACK),
             Piece(PieceType.QUEEN, Color.BLACK), Piece(PieceType.KING, Color.BLACK), Piece(PieceType.BISHOP, Color.BLACK),
             Piece(PieceType.KNIGHT, Color.BLACK), Piece(PieceType.ROOK, Color.BLACK)]
        ]

    def apply_move(self, move: Move):
        start_pos = move.start_position
        end_pos = move.end_position
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece is None:
            raise ValueError("No piece at start position")

        if not piece.is_valid_move(move, self.board):
            raise ValueError("Invalid move")

        self.board[start_pos[0]][start_pos[1]] = None
        self.board[end_pos[0]][end_pos[1]] = piece

        return self.board

    def is_game_over(self):
        return False