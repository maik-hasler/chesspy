import pygame

from chesspy.board import Board
from chesspy.piece import Color, PieceType

class Game:

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Define the colors for the chess board
        self.light_brown = (245, 222, 179)
        self.dark_brown = (139, 69, 19)

        # Set the size of the screen
        self.screen_width = 640
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Create the chess board surface
        self.board_surface = pygame.Surface((640, 640))

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

    def update_board(self, board: Board):
        # Loop through the board
        for row in range(8):
            for column in range(8):
                piece = board.board[row][column]
                if piece is not None:
                    # Get the appropriate image for the piece
                    if piece.color == Color.WHITE:
                        if piece.piece_type == PieceType.PAWN:
                            image = self.white_pawn
                        elif piece.piece_type == PieceType.ROOK:
                            image = self.white_rook
                        elif piece.piece_type == PieceType.KNIGHT:
                            image = self.white_knight
                        elif piece.piece_type == PieceType.BISHOP:
                            image = self.white_bishop
                        elif piece.piece_type == PieceType.QUEEN:
                            image = self.white_queen
                        elif piece.piece_type == PieceType.KING:
                            image = self.white_king
                    else:
                        if piece.piece_type == PieceType.PAWN:
                            image = self.black_pawn
                        elif piece.piece_type == PieceType.ROOK:
                            image = self.black_rook
                        elif piece.piece_type == PieceType.KNIGHT:
                            image = self.black_knight
                        elif piece.piece_type == PieceType.BISHOP:
                            image = self.black_bishop
                        elif piece.piece_type == PieceType.QUEEN:
                            image = self.black_queen
                        elif piece.piece_type == PieceType.KING:
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