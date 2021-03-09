# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:26:10 2021

@author: 426-2019级-1
"""
import socket 

server = socket.socket()
host = 'localhost'
port = 2222
server.bind((host,port))
server.listen(5) 

while True:
    conn,addr = server.accept()
    conn.send('Hello ip:{},port:{},thanks for visiting'.format(addr[0],addr[1]).encode())
    
    while True:
        buff = conn.recv(1024)
        if buff.decode() != 'q':
            conn.send("Hello ip:{},port:{},i've already received your message".format(addr[0],addr[1]).encode())
            print(buff.decode())
        else:
            conn.send("BYE!".encode())
            conn.close()
            break
    