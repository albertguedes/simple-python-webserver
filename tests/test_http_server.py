import unittest
import threading
import time
import requests
from src.http_server import run, HTTPServer, WebServer

class TestWebServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server in a separate thread
        """
        Initializes the web server in a separate thread before executing
        any tests. This ensures that the server is running before any test is executed.
        """
        cls.server = threading.Thread(target=run, kwargs={'server_class': HTTPServer, 'handler_class': WebServer})
        cls.server.daemon = True
        cls.server.start()
        time.sleep(1)  # Waits for the server to start
    
    def test_server_response(self):
        """Checks if the server responds with code 200 and correct HTML."""
        url = "http://localhost:9000"
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World!", response.text)
    
    @classmethod
    def tearDownClass(cls):
        """The server will be manually stopped."""
        # Since HTTPServer does not have an appropriate shutdown method, this test
        # does not properly shut down the server. An improvement would be needed for a clean shutdown.
        pass

if __name__ == "__main__":
    unittest.main()
