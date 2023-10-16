import socket
from _thread import*
import sys
import pickle
from loteriaGame import Game


# # server = '10.45.8.133'
server = '192.168.0.15'
# # server = '192.168.0.1'
# #typically open port, depends on router
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

#store ip addreses of connected clients
connected = set()
#store games
games = {}
#keep track of current id, dont overide games
idCount = 0


def theadedClient(conn,gameId,p):
    global idCount
    #know if we are player 0 or 1
    conn.send(str.encode(str(p)))

    reply = ''
    while True:
        try:

            data = conn.recv(4096).decode()

            #check if game exists, if client disconnects we delete
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset()
                    elif data != 'get':
                        game.play(p,data)

                    # reply = game
                    conn.sendall(pickle.dumps(reply))

            else:
                break
        except:
            break

    print('Lost connection')
    try:
        del games[gameId]
        print('Closing Game',gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print('Connected to: ', addr)

    #keep track of how many people are connected as once
    idCount +=1
    p = 0
    #every two people that connect add two, 
    gameId = (idCount-1)//2
    #if player 1 or player 2, dont have a pair then create new game
    if idCount %2 ==1:
        games[gameId] = Game(gameId)
        print('Creating a new game...')

    else:
        #both players connected start the game
        games[gameId].ready = True
        p = 1

    start_new_thread(theadedClient,(conn,gameId,p))

# # #runs in background, doesnt have to wait to finish executing
# def threadedClient(conn):
# #     #see if we indeed connected, proof and validation
#     conn.send(str.encode('connected'))
# #     # conn.send(username.encode())
# #     # conn.send(str.encode(username))
# #     # conn.send(str.encode(userName))
# #     #keep running while client connected
#     reply = ''
#     while True:
#         try:
#             data = conn.recv(2048)#amount of bits, if you get errors increase size...the larger the size the longer it takes to recieve information
#             # username = data
#             reply = data.decode('utf-8')#encode the information

#             if not data:
#                 #if somenone left or what not, we leave
#                 print('Disconnected')
#                 break
#             else:
#                 # print('Recieved: ',data)
#                 print('Recieved: ',reply)
#                 print('Sending: ',reply)
            
#             conn.sendall(str.encode(reply))#encode string reply into byte

#         except: 
#             break
#     print('Lost Connection')
#     conn.close()

# # currentPlayer = 0
# #continously looking for connections, see if someone connects, and start a new thread or send certain information
# while True:
#     conn,addr = s.accept()
#     print('Connected to: ',addr)#what ip address where connected to

#     #runs this function, does not need threaded client to finish, just adds another thread or process in the background
#     start_new_thread(threadedClient,(conn,))
#     # currentPlayer +=1