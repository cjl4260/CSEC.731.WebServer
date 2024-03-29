'''
Server.py
Charles Lagasse
Start HTTP server
'''

import sys
from pathlib import Path
import Sockets
import Input


def print_usage():
    #Print the usage message

    print("Usage: HTTP_Server.py ip_address port")


def gather_input():
    #Get command line input 
    
  
    input_args = Input.Input_Args()

    if len(sys.argv) == 3:
        ip_address = sys.argv[1]
        port = sys.argv[2]

        input_args.set_ip_address(ip_address)
        input_args.set_port(int(port))
        input_args.set_scheme("http")

  
   
    elif len(sys.argv) == 5:
        ip_address = sys.argv[1]
        port = sys.argv[2]
        x509_path = sys.argv[3]
        x509_private_key_path = sys.argv[4]

        input_args.set_ip_address(ip_address)
        input_args.set_port(int(port))
        input_args.set_scheme("https")
        input_args.set_x509_path(x509_path)
        input_args.set_x509_private_key_path(x509_private_key_path)

        if input_args.get_x509_path == "invalid" or input_args.get_x509_path_private_key == "invalid":
             print_usage()
             exit(1)

    
    else:
        print_usage()
        exit(1)
    
    return input_args


def main():
    input_args = gather_input()
    Sockets.start_server(input_args)

main()