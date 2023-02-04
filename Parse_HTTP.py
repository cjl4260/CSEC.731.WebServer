'''
Parse_HTTP.py
Language: python3
Author: Charles Lagasse
Description: Parses an HTTP request to check its validity 
'''


'''
Imports:
Will need to import sys to get file argument
Will also need to import file for Responses

'''

'''
Function #1

Get input from user
    Input: None
    Using sys get arg from the command line
    Do a check to make sure the arg exists and print the correct usage if it is not
'''

'''
Function #2

Verify Method 
    Input: method as a string
    Verify that the request method is valid
    If not return a 400 error and exit
'''

'''
Function #3

Verify version
    Input: version as a string 
    Verify that the http version is 1.1
    If not return 400 error and exit 
'''

'''
Function #4

Verify request line syntax
    Input: request line as a string 
    Verify that the request line follows below syntax
            Request-Line = Method SP Request-Target SP HTTP-Version CRLF
    If not return 400 error and exit 
'''

'''
Function #5

Verify a single header
    Input: single header as a string 
    Verify that this header is valid
    If not return 400 error and exit
'''

'''
Function #6

Verify all headers
    Input: All headers as an array/list
    Verify that the host header is present and that all other headers are valid
    If not return 400 error and exit
    '''

'''
Function #7
Parse out fields
    Input: entire request as a string
    Parse out headers and request line
    Send them to the other functions for validation
    '''
