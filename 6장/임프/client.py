from socket import *
from _thread import *

HOST = '172.17.12.125'
PORT = 9999

client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.connect((HOST, PORT))

def recv_data(client_socket) :
    while True :
        try:
            data = client_socket.recv(1024)
            print("\nrecive : ",repr(data.decode()))
            print('Send : ', end = ' ')
            
        except ConnectionAbortedError:
            print(">> Disconnected Server")

        except OSError:
            pass
        
        
start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')
print("You can disconnect if you type 'quit'")

while True:
    print('Send : ', end = ' ')
    message = input('')
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())


client_socket.close()