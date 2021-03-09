# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:36:31 2021

@author: 426-2019级-1
"""

import socket


client = socket.socket()
host = 'localhost'
port = 2222

client.connect((host,port))
print(client.recv(1024).decode())

while True:
    string = input()
    client.send(string.encode())
    buf = client.recv(1024).decode() #接受服务器发送的接收到的指令
    print(buf)
    if string == 'q': 
        break
client.close()