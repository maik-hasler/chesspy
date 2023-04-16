from typing import List, Tuple

import pygame

from chesspy.models import Move
from chesspy.pieces.color import Color
from chesspy.pieces.piece import Piece


class Game:
    """Represents a game."""

    def __init__(self, screen):
        """Initializes a new game object."""
        self.screen = screen
        self.board_surface = Game.create_empty_board_surface()
        self.board_copy = None
        self.update_display()

    def update_board(self, board: List[List[Piece]]):
        """Updates the visual chess board with a given 2D board."""
        self.board_surface = Game.create_empty_board_surface()
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if piece is not None:
                    image = Game.get_image_for_piece(piece)
                    self.board_surface.blit(image, (column * 80, row * 80))
        self.update_display()

    def highlight_valid_moves(self, valid_moves: List[Move]) -> None:
        if self.board_copy is not None:
            self.board_surface.blit(self.board_copy, (0, 0))
        self.board_copy = self.board_surface.copy()
        for move in valid_moves:
            row, col = move.end_position
            rect = pygame.Rect(col * 80, row * 80, 80, 80)
            pygame.draw.rect(self.board_surface, (0, 255, 0, 50), rect)
        self.update_display()
    
    def reset_highlights(self):
        if self.board_copy is not None:
            self.board_surface.blit(self.board_copy, (0, 0))
            self.board_copy = None

    def update_display(self):
        self.screen.blit(self.board_surface, (0, 0))
        pygame.display.update()

    @staticmethod
    def create_empty_board_surface():
        light_brown = (245, 222, 179)
        dark_brown = (139, 69, 19)
        board_surface = pygame.Surface((640, 640))
        for row in range(8):
            for column in range(8):
                square_rect = pygame.Rect(column * 80, row * 80, 80, 80)
                if (row + column) % 2 == 0:
                    pygame.draw.rect(board_surface, light_brown, square_rect)
                else:
                    pygame.draw.rect(board_surface, dark_brown, square_rect)
        return board_surface

    @staticmethod
    def get_selected_square() -> Tuple[int, int]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_y // 80
        column = mouse_x // 80
        return (row, column)

    @staticmethod
    def get_image_for_piece(piece: Piece) -> pygame.Surface:
        """Loads the image for the given chess piece."""
        piece_type = type(piece).__name__.lower()
        color = "white" if piece.color == Color.WHITE else "black"
        image_path = f"assets/{color}-{piece_type}.png"
        return pygame.image.load(image_path).convert_alpha()
