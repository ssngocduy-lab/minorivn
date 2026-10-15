import http.server
import socketserver
import webbrowser
from pathlib import Path
import sys

PORT = 8000
DIRECTORY = Path(__file__).parent / "dist"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

def run():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n==========================================")
        print(f" Web server đang chạy tại: {url}")
        print(f" Thư mục phục vụ: {DIRECTORY}")
        print(f" Nhấn Ctrl + C để dừng server.")
        print(f"==========================================\n")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng server.")
            sys.exit(0)

if __name__ == "__main__":
    run()
