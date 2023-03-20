import socket
import threading

class Server():
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(2) # listen for 2 clients

    def accept_clients(self):
        while True:
            client, address = self.socket.accept()
            print(f"Connected to {address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()
    
    def handle_client(self, client):
        # handle client connection here
        pass

if __name__ == '__main__':
    server = Server('127.0.0.1', 8000)
    server.accept_clients()