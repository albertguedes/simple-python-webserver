import unittest
import threading
import time
import requests
from src.http_server import run, HTTPServer, WebServer

class TestWebServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Inicia o servidor em uma thread separada
        cls.server = threading.Thread(target=run, kwargs={'server_class': HTTPServer, 'handler_class': WebServer})
        cls.server.daemon = True
        cls.server.start()
        time.sleep(1)  # Aguarda o servidor iniciar
    
    def test_server_response(self):
        """Verifica se o servidor responde com código 200 e HTML correto."""
        url = "http://localhost:9000"
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World!", response.text)
    
    @classmethod
    def tearDownClass(cls):
        """O servidor será interrompido manualmente."""
        # Como HTTPServer não possui um método de shutdown adequado, este teste
        # não desliga o servidor corretamente. Uma melhoria seria necessária para um desligamento limpo.
        pass

if __name__ == "__main__":
    unittest.main()