import socket
import sys
import game
import game_display
import communication
import settings

HOST, PORT = "localhost", 9999
#data = " ".join(sys.argv[1:])

try:
    game_display.init_everything()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
#main action:

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
        game_display.terminal_game.stdscr.refresh()
        communication.wait_period()

except Exception as e:
    game_display.terminal_game.tear_down_systems()
    print e

game_display.terminal_game.tear_down_systems()

