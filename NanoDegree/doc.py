import socketserver

# Server one 
class SocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    server = socketserver.TCPServer((HOST, PORT), SocketServer)
    server.serve_forever()




# Server two
import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.connection, self.address = self.socket.accept()
        print('Server connected with {}'.format(self.address))

    def send(self, message):
        self.connection.send(message.encode())

    def receive(self):
        return self.connection.recv(1024).decode()

    def close(self):
        self.connection.close()
        
if __name__ == "__main__":
    server = Server('localhost', 8000)
    server.send('Hello World!')
    print(server.receive())
    server.close()