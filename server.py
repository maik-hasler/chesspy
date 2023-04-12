import pickle
import socket

from chesspy.board import Board


class Server():
    """Represents a server."""

    def __init__(self, host: str, port: int) -> None:
        """Initializes a new Server object.

        Args:
            host (str): The host of the server.
            port (int): The port of the server.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(2)
        self.clients = []
        self.board = Board()

    def accept_clients(self):
        while len(self.clients) < 2:
            client, _ = self.socket.accept()

            # Send player index to the client using pickle
            player_index_bytes = pickle.dumps(len(self.clients))
            client.sendall(player_index_bytes)

            self.clients.append(client)

    def _broadcast_board(self):
        board_bytes = pickle.dumps(self.board)
        for client in self.clients:
            client.sendall(board_bytes)

    def start_game(self):
        self._broadcast_board()
        while not self.board.game_over:
            current_player = self.clients[self.board.current_player_index]
            self.handle_client(current_player)
            self.board.current_player_index = (self.board.current_player_index + 1) % 2
            if self.board.is_game_over():
                self.board.game_over = True
            self._broadcast_board()

    def handle_client(self, client):
        client.sendall(b"Your turn. Please enter your move:")
        move = client.recv(1024)
        print(f"Received move from client: {move}")

        # Update the board with the move
        # ...

        # Send the updated board to the clients
        self._broadcast_board()

if __name__ == '__main__':
    server = Server('127.0.0.1', 8000)
    server.accept_clients()
    server.start_game()
