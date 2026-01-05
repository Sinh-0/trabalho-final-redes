import socket
import threading 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(1)
print("servidor aguardando conexões na porta 12345...")

conexao, endereco = servidor.accept()
dados = conexao.recv(1024)
print("Mensagem recebida:", dados.decode())
conexao.close()