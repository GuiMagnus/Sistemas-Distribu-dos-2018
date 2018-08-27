#coding: utf-8
import subprocess
from socket import *

ipName='127.0.0.1'
serverPort = 13000

clientSocket = socket(AF_INET,SOCK_STREAM)

while(True):
	try:
		clientSocket = socket(AF_INET,SOCK_STREAM)
		clientSocket.connect((ipName,serverPort))
		executaComando = input('Digite o Comando a ser executado:')
		print(1)
		if executaComando == 'sair':
			break
		clientSocket.send(executaComando.encode('utf-8'))
		recebeComando = str(clientSocket.recv(2048).decode())
		print(recebeComando)
		if __len__(recebeComando) > 2048:
			while str(clientSocket.recv(2048).decode()):
				recebeComando = str(clientSocket.recv(2048).decode())
				print(recebeComando)
		else:
			print(recebeComando)
		
		clientSocket.close()
	except Exception as e:
		executaComando = input('Digite o Comando a ser executado:')
		print(2)
		if executaComando == 'sair':
			break

		comando = subprocess.getstatusoutput(executaComando)
		print(comando[1])




