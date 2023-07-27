import socket


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)  # show in terminal
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
