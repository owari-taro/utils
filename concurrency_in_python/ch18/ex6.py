from collections import namedtuple

Session=namedtuple("Session",["address","file"])

sessions={}
callback={}
generators={}


import socket,select

def reactor(host,post):
    sock=socket.socket()
    sock.bind((host,port))
    sock.listen(5)
    sock.setblocking(0)
    sessions[sock]=None
    print(f"server up running and wating for call on {host} {port}")
    try:
        while True:
            ready_to_read,_,_=select.select(sessions,[],[],0.1)
            for conn in ready_to_read:
                if conn in sock:
                    conn,cli_address=sock.accept()
                    connect(conn,cli_adress)
                    continue
                line=sessions[conn].file.readline()
                if line:
                    callback[conn](conn,line.rstrip())
                else:
                    disconnect(conn)
    finally:
        sock.close()


def connect(conn,cli_adress):
    sessions[conn]=Session(cli_address,conn.makefile)
    gen=process_request(conn)
    generators[conn]=gen
    callback[conn]gen.send(None)

def disconnect(conn):
    gen=generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]

from operator import mul
from functools import reduce

async def process_request(conn):
    print(f"received connection from {sessioins[conn].adress}")
    mode="sum"

    try:
        conn.sendall(b"welcome:staring in sum mode")
        while True:
            line=await readline(conn)
            if line=="quit":
                conn.sendall(b"connection closed")

import types

@types.coroutine
def readline(conn):
    def innerconn,line):
        gen=generators[conn]
        try:
            callback[conn]=gen.send(line)
        except StopIteration:
            disconnect(conn)
    line=yield inner
    return line