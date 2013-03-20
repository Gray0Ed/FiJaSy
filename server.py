import socket

class Server():
    """tu jest miejsce na docstringa"""
    host = ''
    def __init__(self, port):
        self.s = socket.socket()
        self.port = port
        self.s.bind((self.host, port))
        self.s.listen(3)
        

a = Server(10012)


