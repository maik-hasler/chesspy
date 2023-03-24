import pickle
import socket
from chesspy.game import Game
import time
import pygame
import sys

class Client:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.setblocking(False)
        self.game_over = False
        self.game = Game()

    def send_move(self, move):
        self.socket.sendall(move.encode())

    def receive_message(self):
        while True:
            try:
                message = self.socket.recv(1024)
                if not message:
                    break
                return message.decode()
            except BlockingIOError:
                # The socket is non-blocking and there is no data currently available.
                # Wait for a short delay before retrying.
                time.sleep(0.1)
                continue

    def receive_board(self):
        while True:
            try:
                board_bytes = self.socket.recv(1024)
                if not board_bytes:
                    break
                return pickle.loads(board_bytes)
            except BlockingIOError:
                # The socket is non-blocking and there is no data currently available.
                # Wait for a short delay before retrying.
                time.sleep(0.1)
                continue

    def start_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.set_caption("Hello")

    def close(self):
        self.socket.close()

if __name__ == '__main__':
    client = Client('127.0.0.1', 8000)
    print("Connected to server!")
    client.start_game()
    client.close()