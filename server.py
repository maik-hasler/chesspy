import pickle
import socket

from chesspy.board import Board
from chesspy.move import Move


class Server():
    """Represents a server."""

    def __init__(self, host: str, port: int) -> None:
        """Initializes a new server object."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(2)
        self.clients = []
        self.board = Board()

    def accept_clients(self):
        while len(self.clients) < 2:
            client, _ = self.socket.accept()
            player_index_bytes = pickle.dumps(len(self.clients))
            client.sendall(player_index_bytes)
            self.clients.append(client)

    def broadcast_board(self):
        board_bytes = pickle.dumps(self.board)
        for client in self.clients:
            client.sendall(board_bytes)

    def start_game(self):
        self.broadcast_board()
        while not self.board.game_over:
            current_player = self.clients[self.board.current_player_index]
            self.handle_client(current_player)
            self.board.current_player_index = (self.board.current_player_index + 1) % 2
            if self.board.is_game_over():
                self.board.game_over = True
            self.broadcast_board()

    def handle_client(self, client):
        move = Server.receive_move(client)
        self.board.board = self.board.apply_move(move)

    @staticmethod
    def receive_move(client: socket) -> Move:
        """Receives a move from a connected client."""
        move = None
        while move is None:
            move_bytes = client.recv(1024)
            if not move_bytes:
                raise ConnectionError("Connection to client lost.")
            move = pickle.loads(move_bytes)
        return move
    
if __name__ == '__main__':
    server = Server('127.0.0.1', 8000)
    server.accept_clients()
    server.start_game()
