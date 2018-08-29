#tcp sock.sock() .send() .recv() .close() .bind() .listen() .accept()
import socket
import threading


def tcplink(sock):
    sock.send(b'welcome !\n')
    while 1:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello , %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock,),name='XIANCHENG')
    t.start()
