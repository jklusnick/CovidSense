import os
from bluetooth import getBlueToothValue
from http.server import BaseHTTPRequestHandler, HTTPServer

class requestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
                self.send_response(200)
    def do_GET(self):
        data= getBlueToothValue()
        self.send_response(200)
        print(data)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(data)

os.chdir('.') 
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=requestHandler)
server_object.serve_forever()
