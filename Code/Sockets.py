'''
Sockets.py
Charles Lagasse
Socket Connections
'''

import socket
import ssl
import threading
import Handler


NUM_CONNECTIONS = 5
    

def get_request(sock):
    #Receive data
    return str(sock.recv(1024))


def start_server(input_args):
    #Start the server 

    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args.get_ip_address(), input_args.get_port()))
    srv_sock.listen(NUM_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        if input_args.get_scheme() == "https":
            conn_sock = create_tls_socket(conn_sock, input_args.get_x509_path(), input_args.get_x509_private_key_path())
        t = threading.Thread(target=Handler.handler, args=(conn_sock,))
        t.start()


def create_tls_socket(conn_sock, cert_file, key_file):
    #Create TLS socket
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert_file, keyfile=key_file, password=None)

    return context.wrap_socket(conn_sock, server_side=True)