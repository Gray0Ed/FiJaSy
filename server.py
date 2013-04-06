import SocketServer
import game
import game_display
import communication
import settings

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote: ".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())


HOST, PORT = "localhost", 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

server.serve_forever()

pressed_buttons = []
game = Game(NUMBER_OF_BATTLE_ROWS, NUMBER_OF_BATTLE_COLUMNS, DICTIONARY)

while True:
    pressed_buttons = get_user_input()
    play_game(sock, game, pressed_buttons)
    update_display()

