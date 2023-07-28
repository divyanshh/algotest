import logging
import socket


class SocketService:
    @staticmethod
    def get_connection():
        host = socket.gethostname()
        port = 5000
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)  # listen to single client
        conn, address = server_socket.accept()  # accept new connection
        logging.info("Connection from: " + str(address))
        return conn
