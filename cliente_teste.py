import socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.connect(('localhost', 12345))
cliente.send("Oi, Weslem. Funcionou.".encode())
cliente.close()