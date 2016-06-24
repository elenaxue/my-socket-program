
import socket

Host = 'localhost'
Port = 21567
BufSize = 1024
Addr = (Host, Port)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(Addr)

while True:
	data = input('>')
	if not data:
		break
	print(tcpCliSock.getsockname())
	
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BufSize).decode()
	if not data:
		break

	print(data)

tcpCliSock.close()

