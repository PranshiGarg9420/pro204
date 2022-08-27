from pydoc import cli
import socket
from threading import Thread
from xmlrpc.client import Server

SERVER= None
IP_ADDRESS=None
PORT= None

CLIENTS={}

def acceptConnections():
    global SERVER
    global CLIENTS

    while True:
        player_socket, addr= SERVER.accept()
        player_name= player_socket.recv(1024).decode('utf-8').strip()
        print(player_name)

        if len(CLIENTS.keys())==0 :
            print('PLAYER')
            CLIENTS[player_name]={'player_type':'player1'}
        else:
            print('PLAYER')
            CLIENTS[player_name]={'player_type':'player2'}
        
        CLIENTS[player_name]['player_socket']= player_socket
        CLIENTS[player_name]['player_address']= addr
        CLIENTS[player_name]['player_name']= player_name
        CLIENTS[player_name]['player_turn']= False

        print(f"Connection established with {player_name} : {addr}")


def setup():
    print("\n")
    print("\n\t\t\t\t*** WELCOME TO TAMBOLA GAME *** \n")

    global SERVER
    global IP_ADDRESS
    global PORT

    IP_ADDRESS='127.0.0.1'
    PORT= 6000

    SERVER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)

    print("\n\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS... \n")

    acceptConnections()


setup()

        



