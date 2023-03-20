import socket

class Client:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.game_over = False

    def send_move(self, move):
        self.socket.sendall(move.encode())

    def receive_message(self):
        return self.socket.recv(1024).decode()

    def start_game(self):
        while not self.game_over:
            message = self.receive_message()
            print(message)
            move = input("Enter your move: ")
            self.send_move(move)
            if "Game over!" in message:
                self.game_over = True

    def close(self):
        self.socket.close()

if __name__ == '__main__':
    client = Client('127.0.0.1', 8000)
    print("Connected to server!")
    client.start_game()
    client.close()