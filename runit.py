#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostPort = 8000
hostName = '0.0.0.0'

class RequestHandler(BaseHTTPRequestHandler):
	html_response = """
	<h1>Hello and welcome!</h1>
	<p>Thank you for being here, and viewing me on %s</p>
	<hr/>
	<h4>You are welcome to visit me again on any path you like, maybe: <a href="/here/and/there"> here?</a></h4>
	<h1>TIMES TWO WOW! I work well</h1>
	"""

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(self.html_response % self.path, "utf-8"))
                print("SUPERLOG[INFO]:::::::Served path: %s" % self.path)



def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
