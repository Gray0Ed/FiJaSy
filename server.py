import SocketServer
import game
import game_display
import communication
import settings


init_everything()
game = Game(NUMBER_OF_BATTLE_ROWS, NUMBER_OF_BATTLE_COLUMNS, DICTIONARY)

class MyTCPHandler(SocketServer.BaseRequestHandler):
    self.period = 0
    
    def handle(self):
        period += 1
        if period == PERIODICITY - 1:
            period = 0
            game.singleMove()

        self.data = self.request.recv(1024).strip()
        self.pressed_buttons = get_user_input()
        self.request.sendall(pressed_buttons)

        for ch in pressed_buttons:
            game.charPress(0, ch)

        # getting client info
        
        self.pressed_buttons = self.data

        for ch in pressed_buttons:
            game.charPress(1, ch)

        update_display(game)

HOST, PORT = "localhost", 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

server.serve_forever()


