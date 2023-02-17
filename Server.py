'''
Server.py
Language: python3
Author: Charles Lagasse
Description: Main server file that orchestrates the inner logic 
'''

# Import needed resources


'''
Usage 
    Input: None
    Output: Print correct syntax to use with server 
    Logic:
        Checks for all required command line args and prints the correct syntax if the given are incorrect 
'''

'''
Get Input 
    Input: None
    Output: All command line args parsed out 
    Logic:
        Determines if request is HTTP or HTTPs and parses the args 
        If args are incorrect it calls Usage function to print correct syntax
'''

'''
Main
    Input: None
    Output: None
    Logic:
        Calls get input 
        Passes output into the connection handeler to start the connection
'''

main()