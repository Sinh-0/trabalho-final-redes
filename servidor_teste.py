import socket
import threading 

clientes= []

def gerencia_clientes(conexao, endereco):
    print(f"Conexão de {endereco} estabelecida.")
    while True:
        try:
            dados = conexao.recv(1024)
            if not dados:
               break
            
            for c in clientes:
                if c != conexao:
                    try:
                        c.send(dados)
                    except:
                        if c in clientes:
                            clientes.remove(c)
            
            print(f"Mensagem de {endereco}: {dados.decode()}")
            
        except Exception as e:
            print(f"Erro com {endereco}: {e}")
            break

    print(f"Conexão de {endereco} encerrada.")
    if conexao in clientes:
        clientes.remove(conexao)
    conexao.close()
    


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(5)
print("servidor aguardando conexões na porta 12345...")

while True:
    conexao, endereco = servidor.accept()
    clientes.append(conexao)

    nova_thread = threading.Thread(target=gerencia_clientes, args=(conexao, endereco))
    nova_thread.start()