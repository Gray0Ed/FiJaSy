import SocketServer
import game
import game_display
import communication
import settings


game_display.init_everything()
my_game = game.Game(settings.NUMBER_OF_BATTLE_COLUMNS, settings.DICTIONARY)


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            my_game.singleMove()
            self.data = self.request.recv(1024).strip()

            pressed_buttons = game_display.get_user_input()

            char_to_send = '#'
            for ch in pressed_buttons:
                char_to_send += chr(ch)
            # sending pressed buttons to client
            self.request.sendall(char_to_send)

            for ch in char_to_send:
                my_game.charPress(0, ch)

            # getting client info
            # self.data is already string of chr, no need to call chr()
            opponent_char = self.data
            for ch in opponent_char:
                my_game.charPress(1, ch)

            game_display.update_display(my_game)
            game_display.terminal_game.stdscr.refresh()
            communication.wait_period()


HOST, PORT = "localhost", 9999
try:
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
finally:
    game_display.restore_terminal_display()
