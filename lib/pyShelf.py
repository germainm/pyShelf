#!/usr/bin/python
import os
import zipfile
from http.server import HTTPServer, BaseHTTPRequestHandler
from config import Config
from lib.library import Catalogue
from lib.storage import Storage
config = Config()
Storage = Storage()


class InitFiles:
    """First run file creation operations"""
    def __init__(self, file_array):
        print("Begining creation of file structure")
        for _pointer in file_array:
            if not os.path.isfile(_pointer):
                self.CreateFile(_pointer)

    def CreateFile(self, _pointer):
        """Create the file"""
        if not os.path.isdir(os.path.split(_pointer)[0]):
            os.mkdir(os.path.split(_pointer)[0])
            f = open(_pointer, "w+")
        f.close()


class RequestHandler(BaseHTTPRequestHandler):
    """Request Handler"""
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Welcome To pyShelf!')


class BookServer:
    """HTTP Frontend"""
    def __init__(self):
        self.server_address = ('', 8000)
        self.handler = RequestHandler

    def close_prompt(self):
        """Prompt to close server"""
        close = input("Close Server? y/n")
        if close == 'y':
            self.close()
            return True
        else:
            self.close_prompt()

    def run(self):
        """Start HTTP Server"""
        self.httpd = HTTPServer(self.server_address, self.handler)
        try:
            self.httpd.serve_forever()
            self.httpd.handle_request()
            if self.close_prompt() == True:
                pass
        except KeyboardInterrupt:
            print(KeyboardInterrupt, " Closing Server")
            self.close()
            return False

    def close(self):
        """Stop HTTP Server"""
        try:
            self.httpd.server_close()
            return True
        except Exception:
            return False

