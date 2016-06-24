import socket
import time

Host = 'localhost'
Port = 21567
BufSize = 1024
Addr = (Host, Port)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	data = input('>>>')
	if not data:
		break

	udpCliSock.sendto(data.encode(), Addr)

	if data == 'quit' or data == 'bye':
		break

	data_recv, ser_addr = udpCliSock.recvfrom(BufSize)
	if not data_recv:
		break

	print('%s' % data_recv.decode())
# time.sleep(0.5)
udpCliSock.close()