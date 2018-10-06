#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import socketserver
class Sever_Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).decode('utf-8')
                # self.request.send(self.data).encode('utf-8')
                print(self.data)
            except BaseException as e:
                print(e)

                # self.request.close()
                break


if __name__ == '__main__':

    host=''
    port=8082
    server=socketserver.ThreadingTCPServer((host,port),Sever_Handler)
    server.serve_forever()












