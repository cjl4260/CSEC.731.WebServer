from datetime import datetime


def respond_with_200(body, additional_headers=None):
    response = "HTTP/1.1 200 OK\r\nDate: {}\r\nContent-Length: {}\r\n".format(
        datetime.now().strftime('%a, %d %b %Y %I:%M:%S'), len(body)
    )
    if additional_headers is not None:
        response += "\r\n".join(additional_headers) + "\r\n"
    response += "\r\n" + body
    return response


def respond_with_201(body, location):
    response = "HTTP/1.1 201 Created\r\nContent-Location: {}\r\n\r\n{}".format(
        location, body
    )
    return response


def respond_with_400():
    response = "HTTP/1.1 400 Bad Request\r\n\r\nBad Request"
    return response


def respond_with_403():
    response = "HTTP/1.1 403 Forbidden\r\n\r\nForbidden"
    return response


def respond_with_404():
    response = "HTTP/1.1 404 Not Found\r\n\r\nNot Found"
    return response


def respond_with_411():
    response = "HTTP/1.1 411 Length Required\r\n\r\nLength Required"
    return response


def respond_with_500():
    response = "HTTP/1.1 500 Internal Server Error\r\n\r\nInternal Server Error"
    return response
    

def respond_with_501(body=None):
    if body is None:
        body = "Not Implemented"
    response = "HTTP/1.1 501 Not Implemented\r\n\r\n{}".format(body)
    return response


def respond_with_505():
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n\r\nHTTP Version Not Supported"
    return response
