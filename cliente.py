import socket
import threading

IP_Servidor = '0.tcp.sa.ngrok.io'
porta = 17017

nome_usuario = input("Digite seu nome: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_Servidor, porta))
cliente.send(nome_usuario.encode())

def enviar_mensagens():
    while True:
        try:
            texto = input("Sua mensagem: ")
            if texto:
                mensagem_formatada = f"{nome_usuario}: {texto}"
                cliente.send(mensagem_formatada.encode())
        except:
            break

def receber_mensagens():
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            if mensagem:
                print(f"\n[Atualização]: {mensagem}")
                print("Digite sua mensagem: ", end="", flush=True)
            else:
                break
        except:
            print("Erro na conexão.")
            cliente.close()
            break
  
thread_receber = threading.Thread(target=receber_mensagens)
thread_enviar = threading.Thread(target=enviar_mensagens)   

thread_receber.start()
thread_enviar.start() 