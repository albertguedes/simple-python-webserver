#
# test_http_server.py - Unit tests for http_server.py
# 
import unittest
from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHTTPServer(unittest.TestCase):
    def test_server_start(self):
        """
        Test if the server starts correctly on the specified port.

        This test initializes an HTTPServer instance on localhost at port 9000 and
        handles a single request. It asserts that the server's port is correctly set 
        to 9000, indicating that the server has started on the desired port.
        """
        server = HTTPServer(('localhost', 9000), BaseHTTPRequestHandler)
        server.handle_request()
        self.assertTrue(server.server_port == 9000)

    def test_server_stop(self):
        """
        Test if the server stops correctly on the specified port.

        This test initializes an HTTPServer instance on localhost at port 9000,
        handles a single request, and then stops the server with
        server.server_close(). It asserts that the server's port is correctly set
        to 0, indicating that the server has stopped on the desired port.
        """
        server = HTTPServer(('localhost', 9000), BaseHTTPRequestHandler)
        server.handle_request()
        server.server_close()
        self.assertTrue(server.server_port == 0)

if __name__ == '__main__':
    unittest.main()

# The End