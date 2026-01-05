import socket
import threading

IP_Servidor = 'localhost'
porta = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_Servidor, porta)) 

def receber_mensagens():
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            if mensagem:
                print(f"\nAtualização do quadro de avisos: {mensagem}")
                print("Digite sua mensagem: ", end="")
            else:
                break
        except:
            print("Erro na conexão.")
            cliente.close()
            break

def enviar_mensagens():
    while True:
        try:
            msg = input("Digite sua mensagem: ")
            cliente.send(msg.encode())
        except:
            cliente.close()
            break
  
thread_receber = threading.Thread(target=receber_mensagens)
thread_enviar = threading.Thread(target=enviar_mensagens)   

thread_receber.start()
thread_enviar.start() 