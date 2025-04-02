#!/usr/bin/env python
# coding: utf-8
#
# run.py - Simple python web server to run html page
#
# created: 2025-04-02
# author: Albert R. Carnier Guedes (albert@teko.net.br)
# 
# MIT License
# 
# Copyright (c) 2025 Albert R. Carnier Guedes
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        """
        Handle GET requests.

        This function is a callback for the do_GET method of the BaseHTTPRequestHandler
        class. It is called when a GET request is received from the client.

        This function sends a simple HTML page to the client containing a "Hello World!"
        message.
        """
        html="""
        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PYTHON WEBSERVER</title>
            </head>
            <body>
                <p>Hello World!</p>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Language", "pt-br")
        self.send_header("Content-Encoding", "identity")
        self.send_header("Content-Length", len(html))
        self.end_headers()

        self.wfile.write(bytes(html, "utf-8"))

def run(server_class=HTTPServer, handler_class=WebServer):
    """
    Start the web server with the given server class and handler class.

    The parameters are both optional and default to the built-in
    HTTPServer and WebServer classes.

    The server is run on localhost at port 9000.
    """
    server_address = ('localhost', 9000)
    httpd = server_class(server_address, handler_class)
    print(time.asctime(),"Server running at http://%s:%s/" % server_address)
    httpd.serve_forever()

#
# Init the web server
# 
if __name__ == "__main__":
    run()

# The End