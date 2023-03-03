import logging
import socket
import ssl
import threading
import Parser
import Request_Methods
import Responses

NUM_CONCURRENT_CONNECTIONS = 5

def get_request(sock):
    return str(sock.recv(1024))

def create_tls_socket(conn_sock, cert_file, key_file):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert_file, keyfile=key_file, password=None)
    return context.wrap_socket(conn_sock, server_side=True)

def handler(sock):
    response = ""
    try:
        request = get_request(sock)
        parsed_request = Parser.parse_request(request[2:-1])
        request_line = parsed_request.get_method() + " " + parsed_request.get_request_uri() + " " + parsed_request.get_http_version()
        logging.basicConfig(level=logging.DEBUG, filename='HTTP Server Log.txt', filemode='a', format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info(request_line)
        parsed_request.print_parsed_request()
        if parsed_request.get_response_code() != 200:
            response = Responses.respond_with_500()
        else:
            method = parsed_request.get_method()
        if method == "GET":
         response = Request_Methods.process_GET(parsed_request)
        elif method == "POST":
            response = Request_Methods.process_POST(parsed_request)
        elif method == "PUT":
         response = Request_Methods.process_PUT(parsed_request)
        elif method == "DELETE":
            response = Request_Methods.process_DELETE(parsed_request)
        elif method == "HEAD":
            response = Request_Methods.process_HEAD(parsed_request)
    except Exception:
            response = Responses.respond_with_500()
            sock.send(response.encode())
            sock.close()

def start_server(input_args):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args.get_ip_address(), input_args.get_port()))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)
    while True:
        conn_sock, addr = srv_sock.accept()
        if input_args.get_scheme() == "https":
            conn_sock = create_tls_socket(conn_sock, input_args.get_x509_path(), input_args.get_x509_private_key_path())
        t = threading.Thread(target=handler, args=(conn_sock,))
        t.start()

def return_http_code(response_code):
    if response_code == "400":
        return Responses.respond_with_400()
    elif response_code == "501":
        return Responses.respond_with_501()
    elif response_code == "505":
        return Responses.respond_with_505()