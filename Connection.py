import socket
import ssl
import threading
import Handler


NUM_CONCURRENT_CONNECTIONS = 5


def start_server(input_args):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args.get_ip_address(), input_args.get_port()))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        if input_args.get_scheme() == "https":
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.verify_mode = ssl.CERT_OPTIONAL
            context.load_cert_chain(certfile=input_args.get_x509_path(), keyfile=input_args.get_x509_private_key_path(), password=None)
            conn_sock = context.wrap_socket(conn_sock, server_side=True)
        threading.Thread(target=Handler.handler, args=(conn_sock,)).start()


def get_request(sock):
    return str(sock.recv(1024))
