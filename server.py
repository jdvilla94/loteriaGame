import socket
from _thread import*
import sys


server = '10.45.8.133'
#typically open port, depends on router
port = 5555

#sockets just looks for connections essentially
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conect to IPV4 connection,type, and sock stream is how server string comes in

#next we need to bind server and port to the socket... do try and except to make sure port is available
try:
    s.bind((server,port))
except socket.error as e:
    str(e)

#opens up the port....
s.listen(2)#only allow two e
print('Waiting for a connection, Server Started')

#runs in background, doesnt have to wait to finish executing
def threadedClient(conn):
    #see if we indeed connected, proof and validation
    conn.send(str.encode('connected'))
    #keep running while client connected
    reply = ''
    while True:
        try:
            data = conn.recv(2048)#amount of bits, if you get errors increase size...the larger the size the longer it takes to recieve information
            reply = data.decode('utf-8')#encode the information\
            if not data:
                #if somenone left or what not, we leave
                print('Disconnected')
                break
            else:
                print('Recieved: ',reply)
                print('Sending: ',reply)
            
            conn.sendall(str.encode(reply))#encode string reply into byte

        except: 
            break
    print('Lost Connection')
    conn.close()

#continously looking for connections, see if someone connects, and start a new thread or send certain information
while True:
    conn,addr = s.accept()
    print('Connected to: ',addr)#what ip address where connected to

    #runs this function, does not need threaded client to finish, just adds another thread or process in the background
    start_new_thread(threadedClient,(conn,))