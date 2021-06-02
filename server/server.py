import os
from bluetooth import getBlueToothValue
from http.server import BaseHTTPRequestHandler, HTTPServer

class requestHandler(BaseHTTPRequestHandler):
    def send_cors_headers(self):
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Methods", "GET")
      self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_GET(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()
        data= getBlueToothValue()
        print(data)
        response= {}
        response["status"] = "OK"
        response["body"] = data
        self.wfile.write(repr(data).encode())
        

os.chdir('.') 
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=requestHandler)
server_object.serve_forever()