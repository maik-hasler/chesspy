import pickle
import select
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
        self.socket.listen(1)
        self.clients = []
        self.board = Board()

    def accept_clients(self):
        while len(self.clients) < 2:
            client, address = self.socket.accept()
            print(f"Connected to {address}")
            self.clients.append(client)

        # Send the board object to each client
        for client in self.clients:
            board_bytes = pickle.dumps(self.board)
            client.sendall(board_bytes)

    def start_game(self):
        while not self.board.game_over:
            read_sockets, _, _ = select.select(self.clients, [], [], 0)
            for client in read_sockets:
                self.handle_client(client)
                if self.board.is_game_over():
                    self.board.game_over = True
                    break

    def handle_client(self, client):
        client.sendall(b"Your turn. Please enter your move:")
        move = client.recv(1024)
        print(f"Received move from client: {move}")

        # Update the board with the move
        # ...

        # Send the updated board to the clients
        board_bytes = pickle.dumps(self.board)
        for c in self.clients:
            c.sendall(board_bytes)

if __name__ == '__main__':
    server = Server('127.0.0.1', 8000)
    server.accept_clients()
    server.start_game()
