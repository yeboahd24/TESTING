import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, message):
        self.socket.send(message.encode())

    def receive(self):
        return self.socket.recv(1024).decode()

    def close(self):
        self.socket.close()
        
if __name__ == "__main__":
    client = Client('localhost', 8000)
    client.send('Hello World!')
    print(client.receive())
    client.close()