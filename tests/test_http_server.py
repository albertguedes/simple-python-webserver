#
# test_http_server.py - Unit tests for http_server.py
# 
import unittest
from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHTTPServer(unittest.TestCase):
    def test_server_start(self):
        server = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
        server.handle_request()
        self.assertTrue(server.server_port == 8000)

    def test_server_stop(self):
        server = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
        server.handle_request()
        server.server_close()
        self.assertTrue(server.server_port == 0)

if __name__ == '__main__':
    unittest.main()

# The End