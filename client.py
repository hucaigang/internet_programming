# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:36:31 2021

@author: 426-2019级-1
"""

import socket
import threading

client = socket.socket()
host = 'localhost'
port = 2222


def write_msg():
    while True:
        string = input()
        client.send(string.encode())


def read_msg():
    while True:
        buf =  client.recv(1024)
        print(buf.decode())
    
client.connect((host,port))

t1 = threading.Thread(target = write_msg)
t2 = threading.Thread(target = read_msg)

try:
    t1.start()
    t2.start()
except:
    client.close()

