import unittest
import urllib.request

import httptest

class TestHTTPServer(httptest.Handler):

    def do_GET(self):
        contents = "what up".encode()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", len(contents))
        self.end_headers()
        self.wfile.write(contents)

def main():
    with httptest.Server(TestHTTPServer) as ts:
        with urllib.request.urlopen(ts.url()) as f:
            assert f.read().decode('utf-8') == "what up"

class TestHTTPTestMethods(unittest.TestCase):

    @httptest.Server(TestHTTPServer)
    def test_call_response(self, ts=httptest.NoServer()):
        with urllib.request.urlopen(ts.url()) as f:
            self.assertEqual(f.read().decode('utf-8'), "what up")

if __name__ == '__main__':
    main()
