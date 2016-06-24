
import socket
import time

Host = ''
Port = 21567
BufSize = 1024
Addr = (Host, Port)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(Addr)

while True:
	print('waiting for message...')
	data, cli_addr = udpSerSock.recvfrom(BufSize)
	if data.decode() == 'quit' or data.decode() == 'bye':
		break

	ack_data = '[%s] %s' % (time.ctime(), data.decode())
	# udpSerSock.sendto(ack_data.encode(), cli_addr)
	print('...recv msg %s from %s' % (ack_data, cli_addr))
	
udpSerSock.close()
