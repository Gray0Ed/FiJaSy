import socket
import sys
import game
import game_display
import communication
import setting

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

init_everything()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    sock.connect((HOST,PORT))

#main action:

pressed_buttons = []
game = Game(NUMBER_OF_BATTLE_ROWS, NUMBER_OF_BATTLE_COLUMNS, DICTIONARY)

while True:
    pressed_buttons = get_user_input()
    play_game(sock, game, pressed_buttons)
    update_display(game)


