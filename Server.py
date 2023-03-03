import sys
import Connection
import Inputs


def print_usage():
    print("Usage: HTTP_Server.py ip_address port")


def gather_input():
    input_args = Inputs.Inputs()

    if len(sys.argv) == 3:
        ip_address, port = sys.argv[1:3]
        input_args.set_ip_address(ip_address)
        input_args.set_port(int(port))
        input_args.set_scheme("http")
    else:
        print_usage()
        exit(1)
    
    return input_args


def main():
    input_args = gather_input()
    Connection.start_server(input_args)


if __name__ == "__main__":
    main()
