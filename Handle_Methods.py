'''
Handle_Methods.py
Language: python3
Author: Charles Lagasse
Description: Handles the logic and operations for the various HTTP methods
'''
# Import statments
import Responses
from pathlib import Path

'''
GET Fuction
    Input: parsed request
    Output: HTTP response
    Logic:
        Check to see if file exists(404 error) and if the user has permission to view the file(403 error)
        Return 200 with info 
'''

'''
POST Fuction
    Input: parsed request
    Output: HTTP response including info about the POST 
    Logic:
        Check if content length header is present
        Check if file exists and user has permissions
        Execute put
        Return 200 with info
'''

'''
PUT Fuction
    Input: parsed request
    Output: HTTP response
    Logic:
        Create file
        Write body
        Return 200 with info 
'''

'''
DELETE Fuction
    Input: parsed request
    Output: HTTP response
    Logic:
        Check if file exists
        Delete file
        Return 200 with info
'''

'''
HEAD Fuction
    Input: parsed request
    Output: HTTP response
    Logic:
        Check to see if file exists(404 error) and if the user has permission to view the file(403 error)
        Return 200 with just headers present 


'''