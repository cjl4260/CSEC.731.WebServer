import Responses
import PHP
from pathlib import Path


RESOURCES_DIR_NAME = "Resources"


def process_GET(parsed_request):
    if parsed_request.get_request_uri() == "/":
        parsed_request.set_request_uri("/index.html")

    request_uri = parsed_request.get_request_uri().split("?")[0]
    request_params = parsed_request.get_request_uri().split("?")[1] if len(parsed_request.get_request_uri().split("?")) > 1 else ""

    path = Path.cwd() / RESOURCES_DIR_NAME / request_uri.lstrip("/")
    if not path.exists():
        return Responses.respond_with_404()
    
    if path.suffix == ".php" and request_params:
        php_output_headers, php_output_body = PHP.process_php_file(
            path.name, request_params, parsed_request.get_method(), path.parent)
        return Responses.respond_with_200(php_output_body, additional_headers=php_output_headers)
    else:
        try:
            path.open()
        except PermissionError:
            return Responses.respond_with_403()
        except IsADirectoryError:
            return Responses.respond_with_404()
        return Responses.respond_with_200(path.read_text())


def process_POST(parsed_request):
    content_length = next((header[1] for header in parsed_request.get_headers() if header[0].lower() == "content-length"), None)
    if not content_length:
        return Responses.respond_with_411()

    for header in parsed_request.get_headers():
        if header[0] == "Content-Type" and header[1] != "application/x-www-form-urlencoded":
            return Responses.respond_with_501("Only supported Content-Type is application/x-www-form-urlencoded")

    request_uri_path = Path(parsed_request.get_request_uri())
    resources_dir = Path.cwd() / RESOURCES_DIR_NAME
    if request_uri_path.suffix == ".php":
        php_output_headers, php_output_body = PHP.process_php_file(
            request_uri_path.name, parsed_request.get_body(), parsed_request.get_method(), resources_dir)
        return Responses.respond_with_200(php_output_body, additional_headers=php_output_headers)
    else:
        return_body = "Body passed in:\n\t" + parsed_request.get_body() + "\nRequest-URI: " + parsed_request.get_request_uri()
        return Responses.respond_with_200(return_body)


def process_PUT(parsed_request):
    file_name = Path(parsed_request.get_request_uri().lstrip("/"))
    if file_name.is_dir():
        return Responses.respond_with_404()

    path = Path.cwd() / RESOURCES_DIR_NAME / file_name
    path.write_text(parsed_request.get_body())
    return Responses.respond_with_201(parsed_request.get_body(), str(file_name))


def process_DELETE(parsed_request):
    file_name = Path(parsed_request.get_request_uri().lstrip("/"))
    path = Path.cwd() / RESOURCES_DIR_NAME / file_name
    if not path.exists():
        return Responses.respond_with_404()

    path.unlink()
    return Responses.respond_with_200("Delete Successful")


def process_HEAD(parsed_request):
    return Responses.respond_with_200("")
