from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Pawn(Piece):
    """Represents a pawn piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Pawn object.
        Args:
            color (Color): The color of the Pawn.
        """
        self.color = color
        self.has_moved = False

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a pawn on the chess board.
        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_pos = move.start_position
        end_pos = move.end_position
        dest_piece = board[end_pos[0]][end_pos[1]]

        # Check if destination square is occupied by same color piece
        if dest_piece is not None and dest_piece.color == self.color:
            return False

        # Determine direction of pawn movement based on its color
        direction = 1 if self.color == Color.WHITE else -1

        # Check if pawn is moving one or two squares forward on its first move
        if start_pos[0] + direction == end_pos[0] and start_pos[1] == end_pos[1] and dest_piece is None:
            return True
        elif start_pos[0] + 2*direction == end_pos[0] and start_pos[1] == end_pos[1] and not self.has_moved and board[start_pos[0] + direction][start_pos[1]] is None and dest_piece is None:
            return True

        # Check if pawn is capturing a piece diagonally
        if start_pos[0] + direction == end_pos[0] and abs(start_pos[1] - end_pos[1]) == 1 and dest_piece is not None and dest_piece.color != self.color:
            return True

        return False
