import sys
import Parsed_Request

def print_usage():
    print("Usage: HTTP_Parser.py path_to_http_file")

def gather_input():
    try:
        with open(sys.argv[1], 'rb') as f:
            return f.readlines()
    except (IndexError, FileNotFoundError):
        print_usage()
        sys.exit(1)

def verify_method(method, parsed_request):
    allowed_methods = {
        "GET", "POST", "PUT", "DELETE", "HEAD"
    }
    if method.upper() not in allowed_methods:
        parsed_request.set_response_code(501)
    else:
        parsed_request.set_method(method.upper())

def verify_http_version(http_version, parsed_request):
    if http_version not in ("HTTP/1.1", "HTTP/1.0"):
        parsed_request.set_response_code(505)
    else:
        parsed_request.set_http_version(http_version)

def verify_request_line(request_line, parsed_request):
    request_line = request_line.decode("utf-8")
    parts = request_line.split(" ")
    if len(parts) != 3:
        parsed_request.set_response_code(400)
        return
    verify_method(parts[0], parsed_request)
    parsed_request.set_request_uri(parts[1])
    verify_http_version(parts[2], parsed_request)

def verify_header(header, parsed_request):
    header = header.decode("utf-8").strip()
    parts = header.split(":")
    if len(parts) != 2:
        parsed_request.set_response_code(400)
        return
    header_name, header_value = parts
    parsed_request.set_header(header_name, header_value.strip())

def verify_headers(headers, parsed_request):
    for header in headers:
        verify_header(header, parsed_request)
    if parsed_request.get_http_version() == "HTTP/1.1":
        if not parsed_request.has_header("Host"):
            parsed_request.set_response_code(400)

def parse_request(request):
    parsed_request = Parsed_Request.Parsed_Request()
    lines = request.split(b"\r\n")
    verify_request_line(lines[0], parsed_request)
    verify_headers(lines[1:], parsed_request)
    return parsed_request
import sys
import Parsed_Request

def print_usage():
    print("Usage: HTTP_Parser.py path_to_http_file")

def gather_input():
    try:
        with open(sys.argv[1], 'rb') as f:
            return f.readlines()
    except (IndexError, FileNotFoundError):
        print_usage()
        sys.exit(1)

def verify_method(method, parsed_request):
    allowed_methods = {
        "GET", "POST", "PUT", "DELETE", "HEAD"
    }
    if method.upper() not in allowed_methods:
        parsed_request.set_response_code(501)
    else:
        parsed_request.set_method(method.upper())

def verify_http_version(http_version, parsed_request):
    if http_version not in ("HTTP/1.1", "HTTP/1.0"):
        parsed_request.set_response_code(505)
    else:
        parsed_request.set_http_version(http_version)

def verify_request_line(request_line, parsed_request):
    request_line = request_line.decode("utf-8")
    parts = request_line.split(" ")
    if len(parts) != 3:
        parsed_request.set_response_code(400)
        return
    verify_method(parts[0], parsed_request)
    parsed_request.set_request_uri(parts[1])
    verify_http_version(parts[2], parsed_request)

def verify_header(header, parsed_request):
    header = header.decode("utf-8").strip()
    parts = header.split(":")
    if len(parts) != 2:
        parsed_request.set_response_code(400)
        return
    header_name, header_value = parts
    parsed_request.set_header(header_name, header_value.strip())

def verify_headers(headers, parsed_request):
    for header in headers:
        verify_header(header, parsed_request)
    if parsed_request.get_http_version() == "HTTP/1.1":
        if not parsed_request.has_header("Host"):
            parsed_request.set_response_code(400)

def parse_request(request):
    parsed_request = Parsed_Request.Parsed_Request()
    lines = request.split(b"\r\n")
    verify_request_line(lines[0], parsed_request)
    verify_headers(lines[1:], parsed_request)
    return parsed_request
