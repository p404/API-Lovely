#!python
# -*- coding: utf-8 -*-
# Execute salt-cloud formula for deploying containers
# Usage:
# you need to instal paramiko package
# pip install paramiko -v 1.16.0
# and execute python script '$ python deploy.py'
# for more info about paramiko http://docs.paramiko.org/en/1.16/


import os
import paramiko
import argparse
import sys

if __name__ == '__main__':
    
    # Init vars
	serverip = '52.35.204.170'
	login = 'deploy'
	sshport = 22

	# Parsing input
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="subparser_name")

	cold_parser = subparsers.add_parser('cold')
	cold_parser.add_argument('-n', nargs='+', help='Names for the instances ')

	up_parser = subparsers.add_parser('up')

	args = parser.parse_args()
	
	# Generating the command
	if args.subparser_name == 'up':
	   print "Deploying new containers (All Servers)....."
	   command = """sudo salt '*' state.sls api.docker"""

	if args.subparser_name == 'cold' and args.n is not None:
	   api_string = 'api-'
	   list_names = [api_string + x for x in args.n]
	   appended_list_names = " ".join(list_names)
	   print "Deploying new API instances, this could take a while......."
	   print "Approximate executing time: 10 minutes per instance."
	   command = 'sudo salt-cloud -p api-micro %s' % appended_list_names 
	else:
		sys.exit("You need to add -n and names to the cold command")

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

    # Execute command
	stdin, stdout, stderr = ssh.exec_command(command)
	for line in stdout:
	        print '... ' + line.strip('\n')
	ssh.close()

