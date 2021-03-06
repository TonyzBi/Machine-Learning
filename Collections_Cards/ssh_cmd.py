#!/usr/bin/env python

import pexpect

def ssh_cmd(ip, passwd, cmd):
    ret = -1
    ssh = pexpect.spawn('ssh root@%s "%s"' % (ip, cmd))
    try:
        i = ssh.expect(['Password: ', 'continue connecting (yes/no)?'], timeout = 5)
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('Password: ')
            ssh.sendline(passwd)

        ssh.sendline(cmd)
        r = ssh.read()
        print r
        ret = 0
    except pexpect.EOF:
        print 'EOF'
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        print 'TIMEOUT'
        ssh.close()
        ret = -2
    return ret

ssh_cmd('10.163.140.113', 'ericsson', 'cudbSystemStatus')
