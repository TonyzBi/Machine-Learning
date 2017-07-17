# -*- coding: utf-8 -*-

import SocketServer
import os
import sys

class FtpServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        _base_path = '/Users/administrator/PycharmProjects/'
        if not os.path.exists(_base_path):
            print 'Base Directory is not exist, please choose the right folder'
            sys.exit(-1)

        conn = self.request
        print 'connected ...'
        while True:
            pre_data = conn.recv(1024)
            cmd, file_name, file_size = pre_data.split('|')

            recv_size = 0
            file_dir = os.path.join(_base_path, file_name)
            fp = open(file_dir, 'wb')
            Flag = True

            while Flag:
                if int(file_size) > recv_size:
                    data = conn.recv(1024)
                    recv_size += len(data)
                else:
                    recv_size = 0
                    Flag = False
                    continue
                fp.write(data)

            print '{0} upload successed.'.format(file_name)
            fp.close()
try:
    instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),FtpServerHandler)
    instance.serve_forever()
except KeyboardInterrupt,ki:
    print 'Server stoped....'
    sys.exit(0)


