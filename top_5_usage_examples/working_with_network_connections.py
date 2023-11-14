import socket

with socket.create_connection(('example.com', 80)) as connection:
    connection.sendall(b'Hello, server!')
    data = connection.recv(1024)
# Соединение будет автоматически закрыто после выхода из блока with