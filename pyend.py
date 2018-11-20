#!/usr/bin/python
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer

#ML algo import:
import junpengSimple

PORT_NUMBER = 8081

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*');
        self.end_headers()
        # Send the html message
        slashPos = self.path.index('/',1) #second position of '/' in path
        algo = self.path[1:slashPos]
        usrInp = self.path[slashPos+1:]
        print('algo: '+algo)
        print('usr input: ' + usrInp)
        print(' ')
        if algo == 'wc':
            toRet = junpengSimple.return10(usrInp)
            toRet = str(toRet[0]) + ',' + str(toRet[1])
            self.wfile.write(toRet.encode())
        else:
            if algo == 'mao':
                self.wfile.write('not implement yet'.encode())
            else:
                self.wfile.write('error: no such algorithm'.encode())
        return
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port')
    #Wait forever for incoming htto requests
    server.serve_forever()
except KeyboardInterrupt:
    print('received, shutting down the web server')
    server.socket.close()
