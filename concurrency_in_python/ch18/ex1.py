import socket


def reactor(host,port):
    sock=socket.socket()
    sock.bind((host,port))
    sock.listen(5)
    print(f"server up,running ,and wating for call on {host} {post}")

    try:
        while True:
            conn,cli_address=sock.accept()
            process_request(conn,cli_address)
        finally:
            sock.close()

def process_requeest(conn,cli_address):
    file=conn.makefile()
    print(f"reeived connection from {cli_address}")
    try:
        while True:
            line=file.readline()
            if line:
                line=line.rstrip()
                if line=="quit":
                    conn.sendall(b"connection closed\n")
                    return
                print(f"{cli_address}-->{line}")
                conn.sendall(bin(f"echoed {line}"))