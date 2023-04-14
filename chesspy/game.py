from typing import List, Tuple

import pygame

from chesspy.board import Board
from chesspy.models import Move
from chesspy.pieces.bishop import Bishop
from chesspy.pieces.color import Color
from chesspy.pieces.king import King
from chesspy.pieces.knight import Knight
from chesspy.pieces.pawn import Pawn
from chesspy.pieces.queen import Queen
from chesspy.pieces.rook import Rook


class Game:

    def __init__(self, screen, board_surface):
        self.screen = screen
        self.light_brown = (245, 222, 179)
        self.dark_brown = (139, 69, 19)
        self.board_surface = board_surface
        self.board_copy = None

        # Draw the squares on the chess board
        for row in range(8):
            for column in range(8):
                square_rect = pygame.Rect(column * 80, row * 80, 80, 80)
                if (row + column) % 2 == 0:
                    pygame.draw.rect(self.board_surface, self.light_brown, square_rect)
                else:
                    pygame.draw.rect(self.board_surface, self.dark_brown, square_rect)

        self.black_pawn = pygame.image.load("assets/Black-Pawn.png").convert_alpha()
        self.black_rook = pygame.image.load("assets/Black-Rook.png").convert_alpha()
        self.black_knight = pygame.image.load("assets/Black-Knight.png").convert_alpha()
        self.black_bishop = pygame.image.load("assets/Black-Bishop.png").convert_alpha()
        self.black_queen = pygame.image.load("assets/Black-Queen.png").convert_alpha()
        self.black_king = pygame.image.load("assets/Black-King.png").convert_alpha()
        self.white_pawn = pygame.image.load("assets/White-Pawn.png").convert_alpha()
        self.white_rook = pygame.image.load("assets/White-Rook.png").convert_alpha()
        self.white_knight = pygame.image.load("assets/White-Knight.png").convert_alpha()
        self.white_bishop = pygame.image.load("assets/White-Bishop.png").convert_alpha()
        self.white_queen = pygame.image.load("assets/White-Queen.png").convert_alpha()
        self.white_king = pygame.image.load("assets/White-King.png").convert_alpha()


        # Add the board surface to the screen
        self.screen.blit(self.board_surface, (0, 0))

        # Update the display
        pygame.display.update()

    def update_board(self, board):
        # Loop through the board
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if piece is not None:
                    # Get the appropriate image for the piece
                    if piece.color == Color.WHITE:
                        if isinstance(piece, Pawn):
                            image = self.white_pawn
                        elif isinstance(piece, Rook):
                            image = self.white_rook
                        elif isinstance(piece, Knight):
                            image = self.white_knight
                        elif isinstance(piece, Bishop):
                            image = self.white_bishop
                        elif isinstance(piece, Queen):
                            image = self.white_queen
                        elif isinstance(piece, King):
                            image = self.white_king
                    else:
                        if isinstance(piece, Pawn):
                            image = self.black_pawn
                        elif isinstance(piece, Rook):
                            image = self.black_rook
                        elif isinstance(piece, Knight):
                            image = self.black_knight
                        elif isinstance(piece, Bishop):
                            image = self.black_bishop
                        elif isinstance(piece, Queen):
                            image = self.black_queen
                        elif isinstance(piece, King):
                            image = self.black_king

                    # Calculate the position to blit the image
                    x = column * 80
                    y = row * 80

                    # Blit the image onto the board surface
                    self.board_surface.blit(image, (x, y))

        # Blit the updated board surface onto the screen
        self.screen.blit(self.board_surface, (0, 0))

        # Update the display
        pygame.display.update()

    def highlight_valid_moves(self, valid_moves: List[Move]) -> None:
        if self.board_copy is not None:
            self.board_surface.blit(self.board_copy, (0, 0))
        self.board_copy = self.board_surface.copy()
        for move in valid_moves:
            row, col = move.end_position
            rect = pygame.Rect(col * 80, row * 80, 80, 80)
            pygame.draw.rect(self.board_surface, (0, 255, 0, 50), rect)
        self.screen.blit(self.board_surface, (0, 0))
        pygame.display.update()
    
    @staticmethod
    def get_selected_square() -> Tuple[int, int]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_y // 80
        column = mouse_x // 80
        return (row, column)
    
    def reset_highlights(self):
        if self.board_copy is not None:
            self.board_surface.blit(self.board_copy, (0, 0))