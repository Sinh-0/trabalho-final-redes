import socket
import threading 

clientes= []

def gerencia_clientes(conexao, endereco):
    print(f"Conexão de {endereco} estabelecida.")
    while True:
        try:
            dados = conexao.recv(1024)
        except:
            break
        if not dados:
            break
        print(f"Mensagem de {endereco}: {dados.decode()}")

    for c in clientes:
        if c != conexao:
            try:
                c.send(dados)
            except:
                clientes.remove(c)
except:
    break
print(f"Conexão de {endereco} encerrada.")
clientes.remove(conexao)
conexao.close()



servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(5)
print("servidor aguardando conexões na porta 12345...")

conexao, endereco = servidor.accept()
dados = conexao.recv(1024)
print("Mensagem recebida:", dados.decode())
conexao.close()