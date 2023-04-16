from typing import List, Optional, Tuple

from chesspy.move import Move
from chesspy.pieces.bishop import Bishop
from chesspy.pieces.color import Color
from chesspy.pieces.king import King
from chesspy.pieces.knight import Knight
from chesspy.pieces.pawn import Pawn
from chesspy.pieces.piece import Piece
from chesspy.pieces.queen import Queen
from chesspy.pieces.rook import Rook


class Board:
    """Represents a chess board."""

    def __init__(self) -> None:
        """Initializes a new board object."""
        self.board = Board.create_board()
        self.current_player_index = 0
        self.game_over = False

    def is_game_over(self) -> bool:
        """Checks whether the game is over."""
        return False

    def get_valid_moves(self, position: Tuple[int, int], piece: Piece) -> List[Move]:
        """Returns a list of valid moves for a piece on the board."""
        valid_moves = []
        for row in range(8):
            for col in range(8):
                move = Move(position, (row, col))
                if piece.is_valid_move(move, self.board):
                    valid_moves.append(move)
        return valid_moves

    def get_piece(self, position: Tuple[int, int]) -> Optional[Piece]:
        """Returns the piece at the specified position on the board."""
        row, col = position
        return self.board[row][col]

    def apply_move(self, move: Move) -> List[List[Piece]]:
        """Applies a move to the chess board."""
        start_pos = move.start_position
        end_pos = move.end_position
        piece = self.get_piece(move.start_position)
        if isinstance(piece, Pawn):
            piece.has_moved = True
        self.board[start_pos[0]][start_pos[1]] = None
        self.board[end_pos[0]][end_pos[1]] = piece
        return self.board

    @staticmethod
    def create_board() -> List[List[Piece]]:
        """Creates a board with pieces placed in their initial positions."""
        board = [[None] * 8 for _ in range(8)]
        board[0][0] = Rook(Color.WHITE)
        board[0][1] = Knight(Color.WHITE)
        board[0][2] = Bishop(Color.WHITE)
        board[0][3] = Queen(Color.WHITE)
        board[0][4] = King(Color.WHITE)
        board[0][5] = Bishop(Color.WHITE)
        board[0][6] = Knight(Color.WHITE)
        board[0][7] = Rook(Color.WHITE)
        for col in range(8):
            board[1][col] = Pawn(Color.WHITE)
        board[7][0] = Rook(Color.BLACK)
        board[7][1] = Knight(Color.BLACK)
        board[7][2] = Bishop(Color.BLACK)
        board[7][3] = Queen(Color.BLACK)
        board[7][4] = King(Color.BLACK)
        board[7][5] = Bishop(Color.BLACK)
        board[7][6] = Knight(Color.BLACK)
        board[7][7] = Rook(Color.BLACK)
        for col in range(8):
            board[6][col] = Pawn(Color.BLACK)
        return board
