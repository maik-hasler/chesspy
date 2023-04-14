from typing import List, Optional, Tuple
from chesspy.pieces.king import King
from chesspy.pieces.queen import Queen
from chesspy.pieces.rook import Rook
from chesspy.pieces.bishop import Bishop
from chesspy.pieces.knight import Knight
from chesspy.pieces.pawn import Pawn
from chesspy.pieces.piece import Piece
from chesspy.move import Move
from chesspy.pieces.color import Color


class Board:
    """Represents a chess board."""

    def __init__(self):
        self.game_over = False
        self.board = self._init_board()
        self.current_player_index = 0

    def _init_board(self):
        board = []
        for row in range(8):
            board_row = []
            for col in range(8):
                piece = None
                if row == 0:
                    if col == 0 or col == 7:
                        piece = Rook(Color.WHITE)
                    elif col == 1 or col == 6:
                        piece = Knight(Color.WHITE)
                    elif col == 2 or col == 5:
                        piece = Bishop(Color.WHITE)
                    elif col == 3:
                        piece = Queen(Color.WHITE)
                    elif col == 4:
                        piece = King(Color.WHITE)
                elif row == 1:
                    piece = Pawn(Color.WHITE)
                elif row == 6:
                    piece = Pawn(Color.BLACK)
                elif row == 7:
                    if col == 0 or col == 7:
                        piece = Rook(Color.BLACK)
                    elif col == 1 or col == 6:
                        piece = Knight(Color.BLACK)
                    elif col == 2 or col == 5:
                        piece = Bishop(Color.BLACK)
                    elif col == 3:
                        piece = Queen(Color.BLACK)
                    elif col == 4:
                        piece = King(Color.BLACK)
                board_row.append(piece)
            board.append(board_row)
        return board

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
    
    def get_valid_moves(self, position: Tuple[int, int], piece: Piece) -> List[Move]:
        """Returns a list of valid moves for a piece on the board.

        Args:
            position (Tuple[int, int]): The position of the piece on the board as a tuple of two integers representing
                the row and column index of the square.
            piece (Piece): The piece to get valid moves for.

        Returns:
            List[Move]: A list of valid moves for the piece.
        """
        valid_moves = []
        for row in range(8):
            for col in range(8):
                move = Move(position, (row, col))
                if piece.is_valid_move(move, self.board):
                    valid_moves.append(move)
        return valid_moves

    def get_piece(self, position: Tuple[int, int]) -> Optional[Piece]:
        """Returns the piece at the specified position on the board.

        Args:
            position (Tuple[int, int]): The position on the board as a tuple of two integers representing
                the row and column index of the square.

        Returns:
            Optional[Piece]: The piece at the specified position or None if there is no piece at the position.
        """
        row, col = position
        return self.board[row][col]
    
    def apply_move(self, move: Move):
        start_pos = move.start_position
        end_pos = move.end_position
        piece = self.board[start_pos[0]][start_pos[1]]
        self.board[start_pos[0]][start_pos[1]] = None
        self.board[end_pos[0]][end_pos[1]] = piece
        return self.board