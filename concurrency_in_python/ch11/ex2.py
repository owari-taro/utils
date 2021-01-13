#echo server
import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self,transport):
        peername=transport.get_extra_info("peername")
        print(f"connection from {peername}")
        self.transport=transport

    def data_recieved(self,data):
        message=data.decode()
        print(f"data received {message}")
        self.trasport.write((f"echoed back:{message}").encode(""))
        print("close the client socket")
        self.transort.close()

loop=asyncio.get_event_loop()
coro=loop.create_server(EchoServerClientProtocol,"127.0.0.1",8888)
server=loop.run_until_complete(coro)
print(f"serving on {server.sockets[0].getsockname()}")
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
