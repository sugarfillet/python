import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
s.send(b'hello i am client\n\r')
while True:
	d = s.recv(1024)
	if d:
		s.send(b'hello i am client\n\r')
	else:
		break

s.close()
