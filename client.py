import socket
import sys
import game
import game_display

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


