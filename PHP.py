import os
from pathlib import Path


def process_php_file(request_uri, request_params, http_method, php_files_path):
    php_file_path = find_php_file_path(request_uri.strip('/'), php_files_path)

    php_script_output = ""
    if http_method == "GET":
        handle_environ_vars(php_file_path, request_params, {'REQUEST_METHOD': 'GET'}, remove_vars=True)
        php_script_output = os.popen("php-cgi").read()
    elif http_method == "POST":
        handle_environ_vars(php_file_path, request_params, {'REQUEST_METHOD': 'POST', 'CONTENT_LENGTH': str(len(request_params)), 'CONTENT_TYPE': 'application/x-www-form-urlencoded'}, remove_vars=True)
        php_script_output = os.popen("echo $BODY | php-cgi").read()
    
    return parse_php_output(php_script_output)


def find_php_file_path(file_name, php_files_path):
    globber = php_files_path.rglob(f'{file_name}.php')
    php_file_path = ""
    
    for php_file in globber:
        if php_file.is_file():
            php_file_path = php_file

    return php_file_path


def handle_environ_vars(script_path, request_params, environ_vars, remove_vars=False):
    if remove_vars:
        for var in environ_vars.keys():
            os.environ.pop(var, None)
    else:
        for key, value in environ_vars.items():
            os.environ[key] = value
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REDIRECT_STATUS"] = "0"
        os.environ["BODY"] = request_params


def parse_php_output(php_output_data):
    output_split = php_output_data.split("\n\n")
    body = output_split[1]

    headers = [header.strip() for header in output_split[0].split("\n")]
    
    return headers, body
