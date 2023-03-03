class Parsed_Request:

    def __init__(self):
        self.body = ""
        self.headers = []
        self.http_version = ""
        self.method = ""
        self.response_code = 200
        self.request_uri = ""

    def set_header(self, header_name, header_value):
        self.headers.append((header_name, header_value))

    def get_headers(self):
        return self.headers

    def set_response_code(self, response_code):
        self.response_code = response_code

    def get_response_code(self):
        return self.response_code

    def set_method(self, method):
        self.method = method

    def get_method(self):
        return self.method

    def set_request_uri(self, request_uri):
        self.request_uri = request_uri

    def get_request_uri(self):
        return self.request_uri

    def set_http_version(self, http_version):
        self.http_version = http_version

    def get_http_version(self):
        return self.http_version

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def print_parsed_request(self):
        print(f"Response Code: {self.response_code}")
        print(f"Method: {self.method}")
        print(f"HTTP Version: {self.http_version}")
        print(f"Request URI: {self.request_uri}")
        print("Headers:")
        for header in self.headers:
            print(f"  - {header[0]}: {header[1]}")
        print(f"Body: {self.body}")
