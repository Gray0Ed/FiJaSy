import unittest
import thread
import time
import socket
import threading
from time import sleep
from server import Server

class serverThread(threading.Thread):
      def run(self):
            self.a = Server(10034)
            self.a.listen()

class TestServerCommunication(unittest.TestCase):

      def setUp(self):
            self.th = serverThread()

      def test_send_hello(self):
            self.th.start()
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto('hello', ('127.0.0.1', 10034))
            #nie wiedziec czemu, jesli nie zdazy dostac tej wiadomosci, to sie wiesza?
            sleep(0.1)
            self.assertEqual(self.th.a.buf, "hello")
            sock.sendto('kill server', ('127.0.0.1', 10034))
            self.th.join()

if __name__ == '__main__':
      unittest.main()
