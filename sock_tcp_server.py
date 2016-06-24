
import socket
import time

Host = ''
Port = 21567
Bufsize = 1024
Addr = (Host, Port)


tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(Addr)
tcpSerSock.listen(5)

while True:
	print('waiting for connection...')
	tcpCliSock, CliAddr = tcpSerSock.accept()
	print('...connected from: ' , CliAddr)
	
	while True:
		data = tcpCliSock.recv(Bufsize).decode()
		if not data:
			break

		recvdata = 'hi, you send [%s] %s from %s' %(time.ctime(),data, CliAddr)
		tcpCliSock.send(recvdata.encode())

tcpCliSock.close()
tcpSerSock.close()