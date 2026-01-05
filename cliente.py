import socket
import threading

IP_Servidor = 'localhost'
porta = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_Servidor, porta)) 