'''
Responses.py
Charles Lagasse
HTTP responses 
'''

from datetime import datetime


def respond_200(body, additional_headers=None):
    #Return HTTP 200 
    
    response = "HTTP/1.1 200 OK\r\n"
    response += "Date: " + datetime.now().strftime('%a, %d %b %Y %I:%M:%S') + "\r\n"
    response += "Content-Length: " + str(len(body)) + "\r\n"
    if additional_headers != None:
        for header in additional_headers:
            response += header + "\r\n"
    response += "\r\n"
    response += body
    return response


def respond_201(body, location):
    #Return HTTP 201 
    
    response = "HTTP/1.1 200 Created\r\n"
    response += "Content-Location: " + location + "\r\n"
    response += "\r\n"
    response += body
    return response


def respond_400():
    #Return HTTP 400
  
    response = "HTTP/1.1 400 Bad Request\r\n"
    response += "\r\n"
    response += "Bad Request"
    return response


def respond_403():
    #Return HTTP 403
    
    response = "HTTP/1.1 400 Forbidden\r\n"
    response += "\r\n"
    response += "Forbidden"
    return response


def respond_404():
    #Return HTTP 404
    
    response = "HTTP/1.1 404 Not Found\r\n"
    response += "\r\n"
    response += "Not Found"
    return response


def respond_411():
    #Return HTTP 411

    response = "HTTP/1.1 411 Length Required\r\n"
    response += "\r\n"
    response += "Length Required"
    return response


def respond_500():
    #Return HTTP 500
    
    response = "HTTP/1.1 500 Internal Server Error\r\n"
    response += "\r\n"
    response += "Internal Server Error"
    return response
    

def respond_501(body=None):
    #Return HTTP 501 
    
   
    response = "HTTP/1.1 501 Not Implemented\r\n"
    response += "\r\n"
    if body != None:
        response += body
    else:
        response += "Not Implemented"
    return response


def respond_505():
    #Return HTTP 505
    
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    response += "\r\n"
    response += "HTTP Version Not Supported"
    return response