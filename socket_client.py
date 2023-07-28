import socket
import threading


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if data.lower().strip() == 'bye':
            break
        if data:
            print('Received from server: ' + data)


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input(" -> ")
        client_socket.send(message.encode())

        if message.lower().strip() == 'bye':
            break

    receive_thread.join()
    client_socket.close()


if __name__ == '__main__':
    client_program()
