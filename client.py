import pickle
import socket
from select import select

import pygame

from chesspy.game import Game
from chesspy.models import Move


class Client:
    """Represents a server."""

    def __init__(self) -> None:
        """Initializes a new Client object."""
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.game = Game(self.screen)
        self.board = None

    def connect(self, host: str, port: int) -> None:
        """Connect to a server.

        Args:
            host (str): The host of the associate server.
            port (int): The port of the associate server.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.setblocking(False)

        # Receive player index from the server using pickle
        while True:
            player_index_bytes = self.receive_data()
            if player_index_bytes == None:
                continue
            self.player_index = pickle.loads(player_index_bytes)
            break

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    row = mouse_y // 80
                    column = mouse_x // 80
                    selected_square = (row, column)
                    print(f"You selected {selected_square}")
                    self.game.highlight_moves(self.board, selected_square)
            
            # Check if there is data to be read from the server
            data = self.receive_data()

            if data is None:
                continue

            # Deserialize the board object sent by the server
            self.board = pickle.loads(data)

            # Update the game state here
            self.game.update_board(self.board)

            # Update the screen here
            pygame.display.update()

            # Display a message indicating whose turn it is
            current_player_index = self.board.current_player_index
            if current_player_index == self.player_index:
                message = "Your turn"
            else:
                message = "Opponent's turn"
            font = pygame.font.Font(None, 36) # create a font object
            text_surface = font.render(message, True, (255, 255, 255)) # create a surface with text
            self.screen.blit(text_surface, (100, 100)) # blit the surface onto the screen

    def receive_data(self):
        ready_to_read, _, _ = select([self.socket], [], [], 0)
        for server in ready_to_read:
            data = server.recv(1024)
            if not data:
                return None
            return data

    def disconnect(self):
        """Disconnect from a server."""
        self.socket.close()

if __name__ == '__main__':
    client = Client()
    client.connect('127.0.0.1', 8000)
    client.start_game()
    client.disconnect()
