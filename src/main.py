import pygame

def create_chess_board():
    # Initialize Pygame
    pygame.init()

    # Define the colors for the chess board
    light_brown = (245, 222, 179)
    dark_brown = (139, 69, 19)

    # Set the size of the screen
    screen_width = 640
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create the chess board surface
    board_surface = pygame.Surface((640, 640))

    # Draw the squares on the chess board
    for row in range(8):
        for column in range(8):
            square_rect = pygame.Rect(column * 80, row * 80, 80, 80)
            if (row + column) % 2 == 0:
                pygame.draw.rect(board_surface, light_brown, square_rect)
            else:
                pygame.draw.rect(board_surface, dark_brown, square_rect)

    # Load the chess piece images
    black_pawn = pygame.image.load("../assets/Black-Pawn.png").convert_alpha()
    black_rook = pygame.image.load("../assets/Black-Rook.png").convert_alpha()
    black_knight = pygame.image.load("../assets/Black-Knight.png").convert_alpha()
    black_bishop = pygame.image.load("../assets/Black-Bishop.png").convert_alpha()
    black_queen = pygame.image.load("../assets/Black-Queen.png").convert_alpha()
    black_king = pygame.image.load("../assets/Black-King.png").convert_alpha()
    white_pawn = pygame.image.load("../assets/White-Pawn.png").convert_alpha()
    white_rook = pygame.image.load("../assets/White-Rook.png").convert_alpha()
    white_knight = pygame.image.load("../assets/White-Knight.png").convert_alpha()
    white_bishop = pygame.image.load("../assets/White-Bishop.png").convert_alpha()
    white_queen = pygame.image.load("../assets/White-Queen.png").convert_alpha()
    white_king = pygame.image.load("../assets/White-King.png").convert_alpha()

    # Add the chess pieces to the board surface
    board_surface.blit(black_rook, black_rook.get_rect(center=pygame.Rect(0, 0, 80, 80).center))
    board_surface.blit(black_knight, black_knight.get_rect(center=pygame.Rect(80, 0, 80, 80).center))
    board_surface.blit(black_bishop, black_bishop.get_rect(center=pygame.Rect(160, 0, 80, 80).center))
    board_surface.blit(black_queen, black_queen.get_rect(center=pygame.Rect(240, 0, 80, 80).center))
    board_surface.blit(black_king, black_king.get_rect(center=pygame.Rect(320, 0, 80, 80).center))
    board_surface.blit(black_bishop, black_bishop.get_rect(center=pygame.Rect(400, 0, 80, 80).center))
    board_surface.blit(black_knight, black_knight.get_rect(center=pygame.Rect(480, 0, 80, 80).center))
    board_surface.blit(black_rook, black_rook.get_rect(center=pygame.Rect(560, 0, 80, 80).center))

    # Add the remaining black pawns to the board surface
    for column in range(8):
        board_surface.blit(black_pawn, black_pawn.get_rect(center=pygame.Rect(column * 80, 80, 80, 80).center))

    # Add the white pieces to the board surface
    board_surface.blit(white_rook, white_rook.get_rect(center=pygame.Rect(0, 560, 80, 80).center))
    board_surface.blit(white_knight, white_knight.get_rect(center=pygame.Rect(80, 560, 80, 80).center))
    board_surface.blit(white_bishop, white_bishop.get_rect(center=pygame.Rect(160, 560, 80, 80).center))
    board_surface.blit(white_queen, white_queen.get_rect(center=pygame.Rect(240, 560, 80, 80).center))
    board_surface.blit(white_king, white_king.get_rect(center=pygame.Rect(320, 560, 80, 80).center))
    board_surface.blit(white_bishop, white_bishop.get_rect(center=pygame.Rect(400, 560, 80, 80).center))
    board_surface.blit(white_knight, white_knight.get_rect(center=pygame.Rect(480, 560, 80, 80).center))
    board_surface.blit(white_rook, white_rook.get_rect(center=pygame.Rect(560, 560, 80, 80).center))

    # Add the remaining white pawns to the board surface
    for column in range(8):
        board_surface.blit(white_pawn, white_pawn.get_rect(center=pygame.Rect(column * 80, 480, 80, 80).center))

    # Add the board surface to the screen
    screen.blit(board_surface, (0, 0))

    # Update the display
    pygame.display.update()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    create_chess_board()