import SocketServer
import game


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote: ".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())


HOST, PORT = "localhost", 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

server.serve_forever()


while True:
    pressed_buttons = get_user_input()
    
    for ch in pressed_buttons:
        game.charPress(ch)

