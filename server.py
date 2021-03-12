# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:26:10 2021

@author: 426-2019级-1
"""
import socket 
import threading
import time

def server_init():
    server = socket.socket()
    host = 'localhost'
    port = 2222
    server.bind((host,port))
    server.listen(5)
    return server




def client_handle(con,addr,i):
    con.send('hello {},i have received your message'.format(addr).encode())
    while True:
        try:
            buf = con.recv(1024)
        except:
            print('{} leaves'.format(addr))
            con.close()
            thread_pool.pop(i)
            break
        else:
            print('user {} says:{}'.format(i,buf.decode()))
        
def show_people():
    while True:
        time.sleep(2) #每2秒更新一次在线人数
        print("there are {} people online".format(len(thread_pool)))
        

if __name__ == "__main__":
    server = server_init()
    thread_pool = []
    i = 0
    t1 = threading.Thread(target = show_people)
    t1.start()#线程1 来展示在线人数
    
    while True:
        conn,addr = server.accept() #拥塞IO 服务器在此处等待客户的访问
        t = threading.Thread(target = client_handle,args=(conn, addr, i)) #线程2 处理来访问的客户端 有一个来访问 开启一个新线程
        thread_pool.append(t)#加入线程池
        t.start()#开启该线程
        if thread_pool == []: break
        i+=1
    server.close()