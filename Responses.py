'''
Responses.py
Language: python3
Author: Charles Lagasse
Description: Response codes to send the user. Referenced in Parse_HTTP.py
'''

def Response_Code_200(body):
    response = "HTTP/1.1 200 OK\r\n"
    #response += "Date: " + datetime.now().strftime('%a, %d %b %Y %I:%M:%S') + "\r\n"
    response += "\r\n"
    response += body
    return response

def Response_Code_201(body, location):
   
    response = "HTTP/1.1 201 Created\r\n"
    response += "Content-Location: " + location + "\r\n"
    response += "\r\n"
    response += body
    return response


def Response_Code_400():
    response = "HTTP/1.1 400 Bad Request\r\n"
    response + "\r\n"
    response += "Bad Request"
    response += "\r\n"
    return response

def Response_Code_403():
    response = "HTTP/1.1 400 Forbidden\r\n"
    response + "\r\n"
    response += "Forbidden"
    response += "\r\n"
    return response

def Response_Code_404():
    response = "HTTP/1.1 404 Not Found\r\n"
    response + "\r\n"
    response += "Not Found"
    response += "\r\n"
    return response

def Response_Code_411():
    response = "HTTP/1.1 411 Length Required\r\n"
    response + "\r\n"
    response += "Length Required"
    response += "\r\n"
    return response

def Response_Code_500():
    response = "HTTP/1.1 500 Internal Server Error\r\n"
    response + "\r\n"
    response += "Internal Server Error"
    response += "\r\n"
    return response

def Response_Code_501():
    response = "HTTP/1.1 501 Not Implemented\r\n"
    response + "\r\n"
    response += "Not Implemented"
    response += "\r\n"
    return response

def Response_Code_505():
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    response + "\r\n"
    response += "HTTP Version Not Supported"
    response += "\r\n"
    return response
