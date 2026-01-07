import socket
import threading 

clientes = []

def gerencia_clientes(conexao, endereco):
    try:
        nome_usuario = conexao.recv(1024).decode()
        
        boas_vindas = f"\n[SISTEMA]: {nome_usuario} entrou"
        print(f"[Ativo]: {nome_usuario} ({endereco}) conectado.")
        
        for c in clientes:
            if c != conexao:
                try:
                    c.send(boas_vindas.encode())
                except:
                    pass

        while True:
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
            
            print(f"[Ativo]: {dados.decode()}")
            
    except Exception as e:
        print(f"Erro com {endereco}: {e}")
    finally:
        print(f"Conexão de {nome_usuario} ({endereco}) encerrada.")
        if conexao in clientes:
            clientes.remove(conexao)
        conexao.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(('0.0.0.0', 12345))
servidor.listen(5)
print("Servidor aguardando conexões na porta 12345...")

while True:
    conexao, endereco = servidor.accept()
    clientes.append(conexao)

    nova_thread = threading.Thread(target=gerencia_clientes, args=(conexao, endereco))
    nova_thread.start()