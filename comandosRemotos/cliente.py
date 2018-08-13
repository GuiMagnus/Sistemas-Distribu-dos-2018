#coding: utf-8

from socket import *

ipName='127.0.0.1'
serverPort = 13002

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ipName,serverPort))




while(True):
	executaComando = input('Digite o Comando a ser executado:')

	if executaComando == 'sair':
		break

	clientSocket.send(executaComando.encode('utf-8'))

	recebeComando = str(clientSocket.recv(1024).decode())
	
	print(recebeComando)
clientSocket.close()
