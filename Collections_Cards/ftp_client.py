# -*- coding: utf-8 -*-

import socket
import sys
import os

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)

container = {'key':'', 'data':''}

while True:
    input = raw_input('ftp>')
    cmdString = input.split(' ', 1)

    if len(cmdString) == 1:
        cmd =cmdString[0].strip()
    else:
        cmd, path = cmdString
    # quit Function
    if cmd == 'quit':
        sys.exit(0)
    # show current directory Function
    if cmd == 'pwd':
        print os.getcwd()
        continue
    # 填加切换目录指令
    if cmd == 'cd' and os.path.exists(path):
        os.chdir(path)
        continue

    # list dir Function
    if cmd == 'ls':
        dirs = os.listdir('.')
        for dir in dirs:
            print dir,
        print ''
        continue
    # upload file Function
    if not cmd == 'up' or not os.path.exists(path):
        print 'Error command or File not exist, please check again. '
        continue

    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size

    sk.send(cmd + '|' + file_name + '|' + str(file_size))

    send_size = 0
    fp = open(path, 'rb')

    read_flag = True

    while read_flag:
        if send_size + 1024 > file_size:
            data = fp.read(file_size - send_size)
            read_flag = False

        else:
            data = fp.read(1024)
            send_size += 1024

        sk.send(data)
    # finished to sent file data

    fp.close()

#end

sk.close()


