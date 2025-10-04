import socket
from _thread import *
import threading
from tkinter import *
from time import sleep
import sqlite3

def send(socket):
    global go_send
    while True:
        if go_send:
            message = (message_input.get(1.0,"end")).rstrip()
            socket.send(message.encode())
            message_input.delete(1.0, "end")
            go_send = False
        else:
            if go_out:
                socket.close()
                exit()
            sleep(0.1)

def receive(socket):
    first = True
    while True:
        try:
            data = socket.recv(1024)
            chat_log['state'] = 'normal'
            if first:
                chat_log.insert("end",str(data.decode( )))
                first = False
            else:
                chat_log.insert("end",'\n' + str(data.decode()))
                chat_log.see('end')
            chat_log['state'] = 'disabled'
        except ConnectionAbortedError:
            chat_log['state'] = 'normal'
            chat_log.insert("end", '\n[System] 접속을 종료합니다.\n')
            chat_log['state'] = 'disabled'
            exit()

def login():
    # 서버의 ip주소 및 포트
    HOST = ip_entry.get(); PORT = int(port_entry.get())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=send, args= (client_socket,)).start()
    threading.Thread(target=receive, args= (client_socket,)).start()
    exit()

def try_login():
    global go_out
    start_new_thread(login,())
    server_con['state'] = 'disabled'
    server_discon['state'] = 'active'
    ip_entry['state'] = 'readonly'
    port_entry['state'] = 'readonly'
    go_out = False

def try_logout():
    global go_out
    server_con['state'] = 'active'
    server_discon['state'] = 'disabled'
    ip_entry['state'] = 'normal'
    port_entry['state'] = 'normal'
    go_out = True

def set_go_send(event):
    global go_send
    go_send = True

def log_in():
    idn = id_entry.get()
    pwd = password_entry.get()

    #데이터베이스 연결
    conn = sqlite3.connect("chat member.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #계정 id레코드 읽기
    cursor.execute('select * from meminfo where id = ?', (idn,)) 
    row = cursor.fetchone() 
    conn.close()

    #계정/비번 조사
    if row != None: 
        if idn == row['id'] and pwd == row['password']: 
            frame1.pack_forget()
            frame2.pack_forget()
            frame3.pack(fill="both", expand=True)
        else:
            msg1.pack()
    else:
        msg1.pack()

def log_page():
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack(fill="both", expand=True)

def join():
    frame1.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)

def join_db():
    idn = id_join_entry.get()
    pwd = password_join_entry.get()

    conn = sqlite3.connect('chat member.db') 
    cursor = conn.cursor()
    cursor.execute(''' insert into meminfo (id, password) values(?, ?)''', (idn, pwd))
    msg.pack()
    conn.commit()
    conn.close()

go_out, go_send = False, False
window = Tk()
window.geometry('500x500')
window.title('Client')
window.resizable(False, False)

frame1 = Frame(window, width=500, height=500)
frame1.pack(fill="both",expand= True)

frame2 = Frame(window)
frame2.pack(fill="both")

frame3 = Frame(window)
frame3.pack(fill="both")

'''log in gui'''
Label(frame1, text = 'ID ').place(x=130,y=100)
Label(frame1, text = 'passoword ').place(x=130,y=130)
id_entry = Entry(frame1,width=14)
id_entry.place(x=200,y=100)
password_entry = Entry(frame1,width=14, show='*')
password_entry.place(x=200,y=130)
log_in_bt = Button(frame1,text='Log in', command=log_in).place(x=130,y=160)
join_bt = Button(frame1, text='join', command=join).place(x=200,y=160)
msg1 = Label(frame1, text='log in fail!!')
msg1.pack_forget()

'''join page'''
Label(frame2, text = '회원가입').place(x=230,y=30)
Label(frame2, text = 'ID ').place(x=130,y=100)
Label(frame2, text = 'passoword ').place(x=130,y=130)
id_join_entry = Entry(frame2,width=14)
id_join_entry.place(x=200,y=100)
password_join_entry = Entry(frame2,width=14, show='*')
password_join_entry.place(x=200,y=130)
join_db_bt = Button(frame2,text='회원가입', command=join_db)
join_db_bt.place(x=130,y=160)
log_go_bt = Button(frame2,text='Log page', command=log_page).place(x=200,y=160)
msg = Label(frame2, text='join success!!')
msg.pack_forget()

''' Top Menu '''
Label(frame3, text = 'Server IP : ').place(x=20, y=20)
Label(frame3, text = 'Port : ').place(x=250, y=20)
ip_entry = Entry(frame3, width=14)
ip_entry.place(x=83, y=21)
ip_entry.insert(0,'127.0.0.1')
port_entry = Entry(frame3, width=5)
port_entry.place(x = 290, y=21)
port_entry.insert(0,'9999')
server_con = Button(frame3,text='Log In', command=try_login)
server_con.place(x=350, y=18)
server_discon = Button(frame3,text='Log Out',state = 'disabled', command = try_logout)
server_discon.place(x=420, y=18)

''' Middle Menu '''
chat_frame = Frame(frame3)
scrollbar = Scrollbar(chat_frame) ; scrollbar.pack(side='right',fill='y')
chat_log = Text(chat_frame, width = 62, height = 24, state = 'disabled', yscrollcommand = scrollbar.set) 
chat_log.pack(side='left')
scrollbar['command'] = chat_log.yview
chat_frame.place(x=20, y=60)
message_input = Text(frame3, width = 55, height = 4)
message_input.place(x=20,y = 390)
send_button = Button(frame3, text = 'Send', command = lambda: set_go_send(None))
send_button.place(x=430, y=405)
message_input.bind("<Return>",set_go_send)

''' Bottom Menu '''
close_button = Button(frame3,text='Close',command=exit)
close_button.place(x=200, y = 460)

frame3.mainloop()