import socket
from _thread import *
from tkinter import *

def threaded(client_socket, addr):
    global chat_log
    chat_log['state'] = 'normal'
    chat_log.insert("end", 'Connected by :'+ addr[0] + ':' + str(addr[1]) + '\n')
    chat_log['state'] = 'disabled'
    for c in c_list:
        c.sendall(('[System] ' + str(addr[1]) + ' 님이 접속하였습니다.').encode())
    while 1:
        try:
            data = client_socket.recv(1024)
            chat_log['state'] = 'normal'
            chat_log.insert("end", 'Received from ' + addr[0] + ' : ' + str(addr[1]) + ' :: ' + str(data.decode()) + '\n')
            chat_log['state'] = 'disabled'
            for c in c_list:
                c.sendall((str(addr[1]) + ' : ' + data.decode()).encode())
        except ConnectionResetError as e:
            c_list.remove(client_socket)
            for c in c_list:
                c.sendall(('[System] '+ str(addr[1]) + ' 님이 나갔습니다.').encode())
            chat_log['state'] = 'normal'
            chat_log.insert("end", 'Disconnected by ' + addr[0] + ':' + str(addr[1]) + '\n')
            chat_log['state'] = 'disabled'
            break
    client_socket.close()

def server_open():
    HOST = ip_entry.get(); PORT = int(port_entry.get())
    start_new_thread(make_server,(HOST,PORT))
    open_button['state'] = 'disabled'
    ip_entry['state'] = 'readonly'
    port_entry['state'] = 'readonly'

def server_close():
    exit()

def make_server(HOST, PORT):
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 포트사용중이라 연결할 수 없다는 WinError 10048 에러를 해결하기 위해 필요합니다.
    # 서버 소켓의 SOL_SOCKET의 SO_REUSEADDR(이미 사용중인 포트에 대해서도 바인드 허용) 를 1(True)로 설정하는 것으로 이해
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()
    chat_log['state'] = 'normal'
    chat_log.insert("end", 'Server Start\n')
    chat_log['state'] = 'disabled'

    while 1:
        client_socket, addr = server_socket.accept()
        c_list.append(client_socket)
        start_new_thread(threaded, (c_list[-1], addr))

c_list = []
close = False
server_socket = None

s_root = Tk()
s_root.geometry('500x500')
s_root.title('Server')
s_root.resizable(False, False)

''' Top Menu '''
Label(s_root, text = 'Server IP : ').place(x=20, y=20)
Label(s_root, text = 'Port : ').place(x=250, y=20)
ip_entry = Entry(s_root, width=14, text = '127.0.0.1'); ip_entry.place(x=83, y=21)
ip_entry.insert(0,'127.0.0.1')
port_entry = Entry(s_root, width=5, text = '9999'); port_entry.place(x = 290, y=21)
port_entry.insert(0,'9999')
open_button = Button(s_root,text='Server Open', command=server_open); open_button.place(x=380, y=18)

''' Middle Menu '''
chat_log = Text(s_root, width = 65, height = 29, state = 'disabled', spacing2 = 2) ; chat_log.place(x=20, y=60)

''' Bottom Menu '''
close_button = Button(s_root,text='Server Close',command=server_close); close_button.place(x=200, y = 460)
s_root.mainloop()