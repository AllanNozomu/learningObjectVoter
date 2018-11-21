#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

answers = {}

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path[1:]
        try:
            if path == 'save':
                save()
            else:
                values = path.split('=')
                answers[values[0]] = values[1]
        except:
            self.send_response(500)
            return

        self.send_response(200)
 
        self.send_header('Content-type','text/html')
        self.end_headers()
        print(answers)
        return


def save():
    results = []
    for key in answers:
        if answers[key] != '0':
            results.append(key)

    results.sort()
    f = open('results.json', 'w')
    for res in results:
        f.write('%s\n' % res)
    f.close()

    print('results written')


def read():
    try:
        f = open('results.json', 'r')
        for line in f: 
            answers[line[:-1]] = '1'
        f.close()
    except:
        pass


try:
    read()

    print('starting server...')
    server_address = ('127.0.0.1', 8765)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server in 127.0.0.1 at 8765...')
    httpd.serve_forever()
except:
    httpd.socket.close()
    save()