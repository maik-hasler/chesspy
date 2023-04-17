from chesspy.move import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Pawn(Piece):
    """Represents a pawn piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new pawn object."""
        self.color = color
        self.has_moved = False

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a pawn on the chess board."""
        start_pos, end_pos = move.start_position, move.end_position
        dest_piece = board[end_pos[0]][end_pos[1]]

        if dest_piece and dest_piece.color == self.color:
            return False

        direction = self._get_direction()

        if self._is_moving_one_square_forward(start_pos, end_pos, direction, dest_piece):
            return True

        if self._is_moving_two_squares_forward(start_pos, end_pos, direction, dest_piece, board):
            return True

        if self._is_valid_capture_move(start_pos, end_pos, direction, dest_piece):
            return True

        return False

    def _is_moving_one_square_forward(self, start_pos, end_pos, direction, dest_piece) -> bool:
        """Checks if the pawn is moving one square forward."""
        if start_pos[0] + direction == end_pos[0] and start_pos[1] == end_pos[1] and not dest_piece:
            return True
        else:
            return False

    def _is_moving_two_squares_forward(self, start_pos, end_pos, direction, dest_piece, board) -> bool:
        """Checks if the pawn is moving two squares forward on its first move."""
        if start_pos[0] + 2 * direction == end_pos[0] and start_pos[1] == end_pos[1] and not self.has_moved and not dest_piece and not board[start_pos[0] + direction][start_pos[1]]:
            return True
        else:
            return False

    def _is_valid_capture_move(self, start_pos, end_pos, direction, dest_piece) -> bool:
        """Checks if the pawn is making a valid capture move."""
        if abs(start_pos[1] - end_pos[1]) == 1 and start_pos[0] + direction == end_pos[0] and dest_piece and dest_piece.color != self.color:
            return True
        else:
            return False

    def _get_direction(self) -> int:
        """Determines the direction of pawn movement based on its color."""
        return 1 if self.color == Color.WHITE else -1
