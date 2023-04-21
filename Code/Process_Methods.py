'''
Process_Methods.py
Charles Lagasse
Process HTTP methods 
'''

import Responses
import PHP
from pathlib import Path


RESOURCES_DIR_NAME = "Resources"


def process_GET(parsed_request):
    #Process GET request
    

    if parsed_request.get_request_uri() == "/":
        parsed_request.set_request_uri("/index.html")

    request_uri = parsed_request.get_request_uri().split("?")[0]
    request_params = ""
    if len(parsed_request.get_request_uri().split("?")) > 1:
        request_params = parsed_request.get_request_uri().split("?")[1]

    curr_dir = Path.cwd()
    file_name = Path(request_uri)
    resources_dir = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(resources_dir) + str(file_name))

    if not path.exists():
        return Responses.respond_404()

    if path.suffix == ".php" and request_params != "":
        php_output_headers, php_output_body = PHP.process_php_file(
            file_name.name, request_params, parsed_request.get_method(), resources_dir)
        return Responses.respond_200(php_output_body, additional_headers=php_output_headers)
  
    else:
        try:
            path.open()
        except PermissionError:
            return Responses.respond_403()
        except IsADirectoryError:
            return Responses.respond_404()
        return Responses.respond_200(path.read_text())


def process_POST(parsed_request):
    #Process POST request 
    
    found_content_length = False
    for header in parsed_request.get_headers():
        if header[0].lower() == "content-length":
            found_content_length = True
        if header[0] == "Content-Type" and header[1] != "application/x-www-form-urlencoded":
            return Responses.respond_501("Only supported Content-Type is application/x-www-form-urlencoded")

    if not found_content_length:
        return Responses.respond_411()

    request_uri_path = Path(parsed_request.get_request_uri())
    resources_dir = Path.cwd() / RESOURCES_DIR_NAME
    if request_uri_path.suffix == ".php":
        php_output_headers, php_output_body = PHP.process_php_file(
            request_uri_path.name, parsed_request.get_body(), parsed_request.get_method(), resources_dir)
        return Responses.respond_200(php_output_body, additional_headers=php_output_headers)
    else:
        return_body = "Body passed in:\n\t" + \
            parsed_request.get_body() + \
            "\nRequest-URI: " + \
            parsed_request.get_request_uri()
        return Responses.respond_200(return_body)


def process_PUT(parsed_request):
    #Process PUT request
    
    curr_dir = Path.cwd()
    file_name = Path(parsed_request.get_request_uri())
    path = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(path) + str(file_name))

    if path.is_dir():
        return Responses.respond_404()
    
    body = parsed_request.get_body()
    path.write_text(body)

    return Responses.respond_201(body, str(file_name))


def process_DELETE(parsed_request):
    #Process DELETE request 
    
    curr_dir = Path.cwd()
    file_name = Path(parsed_request.get_request_uri())
    path = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(path) + str(file_name))

    if not path.exists():
        return Responses.respond_404()

    path.unlink()

    return Responses.respond_200("Delete Successfull")


def process_HEAD(parsed_request):
    #Process HEAD request
    
    
    return Responses.respond_200("")