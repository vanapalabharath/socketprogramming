import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

client_socket.connect(server_address)

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                message = data.decode()
                print('Received from server:', message)
            else:
                # Server disconnected
                print('Disconnected from server.')
                client_socket.close()
                break
        except:
            # Server disconnected abruptly
            print('Disconnected from server.')
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input('Enter a message (or "exit" to quit): ')
    client_socket.send(message.encode())
    if message == 'exit':
        break

receive_thread.join()
client_socket.close()

