# Execute salt-cloud formula for deploying containers
# Usage:
# you need to instal paramiko package
# pip install paramiko -v 1.16.0
# and execute python script '$python deploy.py'
# for more info about paramiko http://docs.paramiko.org/en/1.16/

import os
import paramiko

serverip = '10.10.10.10'
login = 'deploy'
sshport = 22
command = 'ls -lah'

# Init then paramiko ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load ssh private key file
privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
private_key = paramiko.RSAKey.from_private_key_file(privatekeyfile)

# Connect and execute the deploy command
ssh.connect(serverip, port=sshport, username=login, pkey=private_key)

# Sends keep alive packets every 20 seconds
ssh.get_transport().set_keepalive(20)

stdin, stdout, stderr = ssh.exec_command(command)

print stdout.read()
