import socket

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_data(self, data):
        self.socket.sendall(data)

    def close(self):
        self.socket.close()

if __name__ == '__main__':
    client = Client('127.0.0.1', 8000)
    client.send_data(b"Hello server")