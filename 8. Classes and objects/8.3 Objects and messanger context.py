from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
# The connection is closed

with conn as s:
    # conn.__enter__() is executed, connection is open
    s.send(b'GET /about/ HTTP/1.0. Other\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.___exit__() is executed, connection is closed
