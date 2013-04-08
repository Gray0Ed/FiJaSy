import unittest
import thread
import time
import socket
import threading
import game
from time import sleep

def wait_period():
    sleep(0.05)

def send_list(sock, ch_list):
    stri = ''
    for c in ch_list:
        stri += chr(c)

    sock.sendall(stri)

def play_game(sock, my_game, pressed_buttons):
    send_list(sock, pressed_buttons)

    for ch in pressed_buttons:
        my_game.charPress(0, chr(ch))
    
    char_to_press = sock.recv(1024)

    for ch in char_to_press:
        my_game.charPress(1, ch)


if __name__ == '__main__':
      unittest.main()

