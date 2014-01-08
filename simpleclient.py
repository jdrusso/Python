import socket
import sys

HOST = '192.168.1.118'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while(1):
	txt = raw_input(">")
	s.send(txt)
