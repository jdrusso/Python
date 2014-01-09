import socket
import sys
import time

HOST = '192.168.1.118'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send('eepread yellow')
while(1):
	
	txt = raw_input(">")
	s.send(txt)

	if txt == 'gogo':
		for x in range(0, 100):
			s.send('eepread red')
			time.sleep(.5)
			s.send('eepread green')
			time.sleep(.5)
			s.send('eepread blue')
			time.sleep(.5)
