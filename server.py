import socket
import os
import mimetypes
from datetime import datetime

HOST, PORT = '127.0.0.1', 8080
BASE_DIR = './www'

def log_request(path, status):
    print(f"[{datetime.now()}] GET {path} - {status}")

def handle_client(client_socket):
    try:
        request_data = client_socket.recv(1024).decode('utf-8', errors='ignore')
        if not request_data:
            return

        lines = request_data.splitlines()
        if len(lines) == 0:
            return

        request_line = lines[0]
        parts = request_line.split()
        if len(parts) < 2:
            return

        method, path = parts[0], parts[1]

        if method != 'GET':
            client_socket.close()
            return

        if path == '/':
            path = '/index.html'

        file_path = os.path.join(BASE_DIR, path.lstrip('/'))

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                body = f.read()

            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'

            headers = [
                "HTTP/1.1 200 OK",
                f"Content-Type: {mime_type}",
                f"Content-Length: {len(body)}",
                "Connection: close",
                "",
                ""
            ]

            response = "\r\n".join(headers).encode('utf-8') + body
            client_socket.sendall(response)
            log_request(path, 200)
        else:
            body = b"<h1>404 Not Found</h1>"
            headers = [
                "HTTP/1.1 404 Not Found",
                "Content-Type: text/html",
                f"Content-Length: {len(body)}",
                "Connection: close",
                "",
                ""
            ]

            response = "\r\n".join(headers).encode('utf-8') + body
            client_socket.sendall(response)
            log_request(path, 404)

    finally:
        client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server in ascolto su http://{HOST}:{PORT}")

        while True:
            client_socket, _ = server_socket.accept()
            handle_client(client_socket)

if __name__ == "__main__":
    start_server()
