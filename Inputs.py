

from pathlib import Path


class Inputs:
    def __init__(self):
        self._ip_address = ""
        self._port = -1
        self._scheme = ""
        self._x509_path = None
        self._x509_private_key_path = None
    
    def set_ip_address(self, ip_address):
        self._ip_address = ip_address
    
    def get_ip_address(self):
        return self._ip_address

    def set_port(self, port):
        self._port = port

    def get_port(self):
        return self._port

    def set_scheme(self, scheme):
        self._scheme = scheme
    
    def get_scheme(self):
        return self._scheme

    def set_x509_paths(self, x509_path, x509_private_key_path):
        pathlib_x509_path = Path(x509_path)
        pathlib_x509_private_key_path = Path(x509_private_key_path)
        if pathlib_x509_path.exists() and pathlib_x509_private_key_path.exists():
            self._x509_path = x509_path
            self._x509_private_key_path = x509_private_key_path
        else:
            self._x509_path = None
            self._x509_private_key_path = None

    def get_x509_path(self):
        return self._x509_path

    def get_x509_private_key_path(self):
        return self._x509_private_key_path

    def print_input_args(self):
        print("IP Address:", self._ip_address)
        print("Port:", self._port)
        print("Scheme:", self._scheme)
        print("x509 Path:", self._x509_path)
        print("x509 Private Key Path:", self._x509_private_key_path)
