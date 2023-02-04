'''
Responses.py
Language: python3
Author: Charles Lagasse
Description: Response codes to send the user. Referenced in Parse_HTTP.py
'''

def Response_Code_200():
    print("HTTP/1.1 200 OK\r\n\r\n")
    exit(0)

def Response_Code_400():
    print("HTTP/1.1 400 BAD REQUEST\r\n\r\n")
    exit(1)

def Response_Code_500():
    print("HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n")
    exit(2)
