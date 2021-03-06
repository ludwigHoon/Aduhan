#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import parser

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"
        try:
            if self.path.endswith(".html"):
                mimetype='text/html'
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
            if self.path.endswith(".gif"):
                mimetype='image/gif'
            if self.path.endswith(".js"):
                mimetype='application/javascript'
            if self.path.endswith(".css"):
                mimetype='text/css'
            #Open the static file requested and send it
            f = open(curdir + sep + self.path, 'rb') 
            self.send_response(200)
            self.send_header('Content-type',mimetype)
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    #Handler for the POST requests
    def do_POST(self):
        #if self.path=="/send":
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>POST!</h1><pre>" + str(post_data) + "</pre></body></html>", 'utf-8'))
        return


try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()