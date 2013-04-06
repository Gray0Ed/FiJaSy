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
    sock.sendall(data+"\n")

    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)

#main action:

pressed_buttons = []
game = Game(
while True:
    pressed_buttons = get_user_input()
    
    for ch in pressed_buttons:
        game.charPress(ch)


