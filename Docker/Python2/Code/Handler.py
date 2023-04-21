'''
Handler.py
Charles Lagasse
Process Requests
'''

import logging
import Sockets
import Parser
import Responses
import Process_Methods


def handler(sock):
    #Process request
    
    response = ""
    try:
        request = Sockets.get_request(sock)

        parsed_request = Parser.parse_request(request[2:-1])

        request_line = parsed_request.get_method() + " " + parsed_request.get_request_uri() + " " + parsed_request.get_http_version()
        log_data(request_line)

        parsed_request.print_parsed_request()
        print()

        if parsed_request.get_response_code() != 200:
            response = return_http_code(parsed_request.get_response_code())
        else:
            response = execute_method(parsed_request)
    except Exception:
        response = Responses.respond_500()

    sock.send(response.encode())
    sock.close()


def log_data(first_line_of_request):
    #Log request
   
    logging.basicConfig(level=logging.DEBUG, filename='HTTP Server Log.txt', filemode='a', format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(first_line_of_request)


def return_http_code(response_code):
    #Return a response code
    
    if response_code == "400":
        return Responses.respond_400()
    elif response_code == "501":
        return Responses.respond_501()
    elif response_code == "505":
        return Responses.respond_505()


def execute_method(parsed_request):
    #Execute HTTP method
    
   
    response = ""
    method = parsed_request.get_method()
    if method == "GET":
        response = Process_Methods.process_GET(parsed_request)
    elif method == "POST":
        response = Process_Methods.process_POST(parsed_request)
    elif method == "PUT":
        response = Process_Methods.process_PUT(parsed_request)
    elif method == "DELETE":
        response = Process_Methods.process_DELETE(parsed_request)
    elif method == "HEAD":
        response = Process_Methods.process_HEAD(parsed_request)
    
    return response