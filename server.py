import socket

class Server():
    """tu jest miejsce na docstringa"""
    host = ''
    def __init__(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = port
        self.s.bind((self.host, port))
        self.buf = ''

    def listen(self):
          while True:
                data, addr = self.s.recvfrom(1024); #buffer size
                print "received:", data, "from", addr
                if self.do(data) == False:
                      break

    def do(self, data):
          print "doing", data
          if data == "kill server":
                return False
          self.buf += data
          return True

#UDP_PORT = 10003;
#a = Server(UDP_PORT)
#a.listen()

