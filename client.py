import socket
import sys
import game
import game_display
import communication
import settings


if len(sys.argv) > 2:
    HOST, PORT = sys.argv[1], int(sys.argv[2])
else:
    HOST, PORT = "192.168.0.10", 9999

try:
    game_display.init_everything()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    # main action:

    pressed_buttons = []
    my_game = game.Game(settings.NUMBER_OF_BATTLE_COLUMNS, settings.DICTIONARY)
    game_display.update_display(my_game)
    while True:
        my_game.singleMove()
        pressed_buttons = game_display.get_user_input()
        char_to_send = '#'
        for ch in pressed_buttons:
            char_to_send += chr(ch)

        sock.sendall(char_to_send)

        for ch in char_to_send:
            my_game.charPress(0, ch)

        opponent_char = sock.recv(1024)

        for ch in opponent_char:
            my_game.charPress(1, ch)

        game_display.update_display(my_game)
        communication.wait_period()
finally:
    game_display.restore_terminal_display()
