import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

server_socket.bind(server_address)

server_socket.listen(5)
print("Server is up and running. Waiting for a connection...")


client_sockets = []
while True:
    client_socket, client_address = server_socket.accept()
    print('Connected by:', client_address)
    client_sockets.append(client_socket)
    welcome_message = 'Welcome to the server!'
    client_socket.send(welcome_message.encode())

    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                # Broadcasting  the message to all connected clients
                message = data.decode()
                print('Received from {}: {}'.format(client_address, message))
                for client in client_sockets:
                    if client != client_socket:
                        client.send(message.encode())
            else:
                # disconnecting client
                client_sockets.remove(client_socket)
                client_socket.close()
                print('Client {} disconnected.'.format(client_address))
                break
        except:
            # Client disconnected abruptly
            client_sockets.remove(client_socket)
            client_socket.close()
            print('Client {} disconnected.'.format(client_address))
            break

server_socket.close()

