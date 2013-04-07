import SocketServer
import game
import game_display
import communication
import settings


game_display.init_everything()
my_game = game.Game(settings.NUMBER_OF_BATTLE_COLUMNS, settings.DICTIONARY)

class MyTCPHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):

        my_game.singleMove()
        self.data = self.request.recv(1024).strip()
        
        #self.pressed_buttons = communication.get_user_input()
        #self.request.sendall(pressed_buttons)

        #for ch in pressed_buttons:
        #    my_game.charPress(0, ch)

        # getting client info
        
        #self.pressed_buttons = self.data
        game_display.update_display(my_game)
        game_display.terminal_game.stdscr.refresh()


HOST, PORT = "localhost", 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

server.serve_forever()


