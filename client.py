import pickle
import socket
from select import select

import pygame

from chesspy.game import Game
from chesspy.move import Move
from chesspy.pieces.color import Color


class Client:
    """Represents a server."""

    def __init__(self) -> None:
        """Initializes a new client object."""
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.game = Game(self.screen)
        self.board = None
        self.socket = None
        self.player_index = None

    def connect(self, host: str, port: int) -> None:
        """Connects to a server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.setblocking(False)
        while self.player_index == None:
            if (player_index_bytes := self.receive_data()) != None:
                self.player_index = pickle.loads(player_index_bytes)

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    current_player_index = self.board.current_player_index
                    if current_player_index == self.player_index:
                        self.selected_square = Game.get_selected_square()
                        piece = self.board.get_piece(self.selected_square)
                        if piece is None or piece.color != Color(self.player_index):
                            continue
                        self.valid_moves = self.board.get_valid_moves(self.selected_square, piece)
                        self.game.highlight_valid_moves(self.valid_moves)
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_player_index = self.board.current_player_index
                    if current_player_index == self.player_index:
                        end_square = Game.get_selected_square()
                        if self.selected_square is not None and end_square != self.selected_square:
                            move = Move(self.selected_square, end_square)
                            if move in self.valid_moves:
                                self.send_move(move)
                        self.game.reset_highlights()
                        self.selected_square = None
            data = self.receive_data()
            if data is None:
                continue
            self.board = pickle.loads(data)
            self.game.update_board(self.board.board)
            pygame.display.update()

    def receive_data(self):
        """Receives data from the connected server."""
        sockets, _, _ = select([self.socket], [], [], 0)
        for server in sockets:
            data = server.recv(1024)
            if not data:
                return None
            return data
        
    def send_move(self, move: Move):
        """Sends a move to the connected server."""
        move_bytes = pickle.dumps(move)
        self.socket.send(move_bytes)

    def disconnect(self):
        """Disconnects from a server."""
        self.socket.close()

if __name__ == '__main__':
    client = Client()
    client.connect('127.0.0.1', 8000)
    client.start_game()
    client.disconnect()
