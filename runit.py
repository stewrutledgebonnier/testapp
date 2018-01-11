#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import logging


hostPort = 8000
hostName = '0.0.0.0'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - TestApp - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

class RequestHandler(BaseHTTPRequestHandler):
    html_response = """
        <h2>Headers:</h2>
        <ol>{}</ol>
    """

    def do_GET(self):
        logger.debug("Processing request")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        headers = ""
        for header in self.headers.items():
            headers += "<li>{}: {}</li>".format(header[0], header[1])
        self.wfile.write(bytes(self.html_response.format(headers), "utf-8"))
        logger.info("Served path: %s" % self.path)



def run(server_class=HTTPServer, handler_class=RequestHandler):
    logger.info("Starting server")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    logger.info("Serving from port 8000")
    httpd.serve_forever()

while True:
    run()
