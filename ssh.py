#!/usr/bin/python

import pexpect

passwd = ""
var = "xxx"

def ssh_cmd(ip,cmd):
  ssh = pexpect.spawn('ssh %s "%s"' % (ip,cmd))
  try:
    i = ssh.expect(['Password:', 'continue connecting (yes/no)?'],timeout=5) 
    if i == 0:
      ssh.sendline(passwd)
    elif i == 1:
      ssh.sendline('yes')
      ssh.expect('Password: ')
      ssh.sendline(passwd)
  except pexpect.EOF:
    print "EOF"
  except pexpect.TIMEOUT:
    print "TIMEOUT"
  else:
    r = ssh.read()
    print r
  ssh.close

ssh_cmd("localhost","ls")
