'''
Parse_HTTP.py
Language: python3
Author: Charles Lagasse
Description: Parses an HTTP request to check its validity 
'''


import sys
import Responses

'''
Function #1

Get input from user
    Input: None
    Using sys get arg from the command line
    Do a check to make sure the arg exists and print the correct usage if it is not
'''
def get_input():
    return open("Good_Requests/complex.txt", 'rb').readlines()
    if len(sys.argv) != 2:
         print("HTTP file not specified\n Usage: Parse_HTTP.py <path to file>")
         exit(1)
    else:
        return open(sys.argv[1], 'rb').readlines()
    

'''
Function #2

Verify Method 
    Input: method as a string
    Verify that the request method is valid
    If not return a 400 error and exit
'''

def validate_method(method):
    valid_methods = [
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "CONNECT",
        "HEAD"
    ]

    if method.upper() not in valid_methods:
        Responses.Response_Code_400()


'''
Function #3

Verify version
    Input: version as a string 
    Verify that the http version is 1.1
    If not return 400 error and exit 
'''

def validate_version(version):
    if version != "HTTP/1.1":
        Responses.Response_Code_400()

'''
Function #4

Verify request line syntax
    Input: request line as a string 
    Verify that the request line follows below syntax
            Request-Line = Method SP Request-Target SP HTTP-Version CRLF
    If not return 400 error and exit 
'''

def validate_request_line(request_line):
    if request_line.count(" ") != 2:
        Responses.Response_Code_400()
    
    split_request_line = request_line.split(" ")
    method = split_request_line[0]
    validate_method(method)

    version = split_request_line[2]
    validate_version(version)

'''
Function #5

Verify a single header
    Input: single header as a string 
    Verify that this header is valid
    If not return 400 error and exit
'''

def validate_header(header):

    value = header.replace(" ", "").split(":")[0]
    if value.upper() == "HOST":
        return 0
    return 1

'''
Function #6

Verify all headers
    Input: All headers as an array/list
    Verify that the host header is present and that all other headers are valid
    If not return 400 error and exit
    '''

def validate_headers(headers):
    valid = 0
    for header in headers:
        valid += validate_header(header)
    if valid != 1:
        Responses.Response_Code_400()
'''
Function #7
Parse out fields
    Input: entire request as a string
    Parse out headers and request line
    Send them to the other functions for validation
    '''
def parse_request_fields(request):
    parsed = ""
    for line in request:
        parsed += str(line)[2:-1]

    if parsed.count("\\r\\n\\r\\n") != 1:
        Responses.Response_Code_400()
    
    request_line = parsed.split("\\r\\n")[0]
    validate_request_line(request_line)

    headers = parsed.split("\\r\\n")[1:-1]
    validate_headers(headers)

    Responses.Response_Code_200()

def main():
    try:
        file = get_input()
        parse_request_fields(file)
    except Exception:
        Responses.Response_Code_500()

main()