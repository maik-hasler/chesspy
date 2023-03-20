import socket
from chesspy.game import Game

class Server():
    
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.clients = []
        self.game = Game()

    def accept_clients(self):
        while len(self.clients) < 2:
            client, address = self.socket.accept()
            print(f"Connected to {address}")
            self.clients.append(client)

    def start_game(self):
        while not self.game.game_over:
            for client in self.clients:
                self.handle_client(client)
                if self.game.is_game_over():
                    self.game.game_over = True
                    break

    def handle_client(self, client):
        client.sendall(b"Your turn. Please enter your move:")
        move = client.recv(1024)
        print(f"Received move from client: {move}")

if __name__ == '__main__':
    server = Server('127.0.0.1', 8000)
    server.accept_clients()
    server.start_game()