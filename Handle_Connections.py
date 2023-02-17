
'''
Handle_Connections.py
Language: python3
Author: Charles Lagasse
Description: Handles socket programming to make the network connection 
'''

#Import needed resources

'''
Logging
    Input: Request Line from HTTP request
    Output: None
    Logic:
        Add the request line from an http request to the log file along with the date
'''

'''
Handler
    Input: Socket
    Output: None
    Logic:
        Socket handlder for multithreaded programming
            Get the request data
            Parse it
            Execute desired method
'''

'''
Response Codes
    Input: response code
    Output: HTTP response for specified error code 
    Logic:
        Check with response code is and call Response file for corresponding HTTP message
'''

'''
Execute Method
    Input: Parsed request
    Output: HTTP response message for corresponding method
    Logic:
        Check method and send the parsed request to the correct funciton in Handle_Methods.py
'''

'''
Get Data
    Input: Socket
    Output: Data sent to server from client 
    Logic:
        sock.recv
'''

'''
Start Server
    Input: Command Line Args
    Output: None
    Logic:
        Create socket 
        Start handler
'''

'''
TLS Socket
    Input: Socket, cert file, key file
    Output: SSL Context
    Logic:
        Using arguments supplied wrap the socket in the TLS context 
'''