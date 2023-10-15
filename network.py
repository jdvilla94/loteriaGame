import socket
from _thread import*

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.server = '10.45.8.133'
        self.server = '192.168.0.15'
        self.port = 5555
        self.addr = (self.server,self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


# n = Network()
# print(n.send('HELLO'))
# print(n.send('WORKING'))



    
