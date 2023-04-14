from abc import ABC, abstractmethod
from enum import Enum

from chesspy.move import Move


class Color(Enum):
    """Enumeration representing the two colors of chess pieces."""

    WHITE = 1
    BLACK = 2

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
    
class Knight(Piece):
    """Represents a knight piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Knight object.

        Args:
            color (Color): The color of the Knight.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a knight on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the move is within the knight's range of movement
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Check if the knight can capture a piece on the end position
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True
            # The knight can move to an empty square
            elif board[end_row][end_col] is None:
                return True
        return False

class Bishop(Piece):
    """Represents a bishop piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Bishop object.

        Args:
            color (Color): The color of the Bishop.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a bishop on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the move is diagonal
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False

        # Check if there are any pieces in the way
        if start_row < end_row:
            row_step = 1
        else:
            row_step = -1
        if start_col < end_col:
            col_step = 1
        else:
            col_step = -1
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step

        # Check if the bishop can capture a piece on the end position
        if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True

        return True

class Rook(Piece):
    """Represents a rook piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Rook object.

        Args:
            color (Color): The color of the Rook.
        """
        self.color = color
    
    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a rook on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the move is a valid rook move
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position
        if start_row != end_row and start_col != end_col:
            return False
        
        # Check if there are any pieces in the way of the move
        if start_row == end_row:
            # Horizontal move
            start_col, end_col = sorted([start_col, end_col])
            for col in range(start_col+1, end_col):
                if board[start_row][col] is not None:
                    return False
        else:
            # Vertical move
            start_row, end_row = sorted([start_row, end_row])
            for row in range(start_row+1, end_row):
                if board[row][start_col] is not None:
                    return False

        # Check if the rook can capture a piece on the end position
        if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True

        return True

class Queen(Piece):
    """Represents a queen piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new Queen object.

        Args:
            color (Color): The color of the Queen.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a queen on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position

        # Check if the move is diagonal
        if abs(end_row - start_row) == abs(end_col - start_col):
            # Check if there are pieces in the way of the diagonal move
            if end_row > start_row and end_col > start_col:
                for i in range(1, end_row - start_row):
                    if board[start_row+i][start_col+i] is not None:
                        return False
            elif end_row > start_row and end_col < start_col:
                for i in range(1, end_row - start_row):
                    if board[start_row+i][start_col-i] is not None:
                        return False
            elif end_row < start_row and end_col > start_col:
                for i in range(1, start_row - end_row):
                    if board[start_row-i][start_col+i] is not None:
                        return False
            else:
                for i in range(1, start_row - end_row):
                    if board[start_row-i][start_col-i] is not None:
                        return False
            return True

        # Check if the move is horizontal or vertical
        if start_row == end_row:
            # Check if there are pieces in the way of the horizontal move
            if end_col > start_col:
                for i in range(start_col+1, end_col):
                    if board[start_row][i] is not None:
                        return False
            else:
                for i in range(end_col+1, start_col):
                    if board[start_row][i] is not None:
                        return False
            return True
        elif start_col == end_col:
            # Check if there are pieces in the way of the vertical move
            if end_row > start_row:
                for i in range(start_row+1, end_row):
                    if board[i][start_col] is not None:
                        return False
            else:
                for i in range(end_row+1, start_row):
                    if board[i][start_col] is not None:
                        return False
            return True

        return False

class King(Piece):
    """Represents a king piece."""

    def __init__(self, color: Color) -> None:
        """Initializes a new King object.

        Args:
            color (Color): The color of the King.
        """
        self.color = color

    def is_valid_move(self, move: Move, board) -> bool:
        """Determines whether a given move is valid for a king on the chess board.

        Args:
            move (Move): The move to be checked.
            board (Board): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_row, start_col = move.start_position
        end_row, end_col = move.end_position

        # Check if the move is within the King's range of movement
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if row_diff <= 1 and col_diff <= 1:
            # Check if there are any pieces blocking the King's way
            if board[end_row][end_col] is not None and board[end_row][end_col].color == self.color:
                return False
            if row_diff == 0 and col_diff == 0:
                return False
            return True

        return False
