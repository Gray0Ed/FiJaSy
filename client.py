import socket
import sys
import game
import game_display
import communication
import settings

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

try:
#init_everything()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOST,PORT))
#main action:

    pressed_buttons = []
    game = game.Game(settings.NUMBER_OF_BATTLE_COLUMNS, settings.DICTIONARY)

    period = 0

    while True:
        period += 1
        if period == PERIODICITY - 1:
            period = 0
            game.singleMove()


        pressed_buttons = game_display.get_user_input()
        play_game(sock, game, pressed_buttons)
        update_display(game)
        communication.wait_period()

except Exception as e:
    print e
