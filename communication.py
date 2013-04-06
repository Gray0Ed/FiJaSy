import unittest
import thread
import time
import socket
import threading
from time import sleep

def send_list(sock, ch_list):
    sock.sendall(sock)

def get_opponent_input(sock):
    return sock.recv(1024)

def play_game(sock, game, pressed_buttons):
    send_list(sock, pressed_buttons)

    for ch in pressed_buttons:
        game.charPress(0, ch)
    
    pressed_buttons = get_opponent_input()

    for ch in pressed_buttons:
        game.charPress(1, ch)


if __name__ == '__main__':
      unittest.main()
