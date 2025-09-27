from tkinter import*
from PIL import ImageTk,Image
import os

os.chdir("C:\\Users\\thgh\\Documents\\프로그래밍1\\자료")

def show_monster(m):
    new_window=Tk()
    new_window.title("game")
    new_window.geometry("500x500")
    if m == 1:
        global img
        img=ImageTk.PhotoImage(file="슬라임.png",master=new_window)
        img_resize=img.resize((int(img.width/2),int(img.height/2)))
        Button(new_window,width=300,height=300,image=img_resize).pack()


window=Tk()
window.title("game")
window.geometry("500x160")
window.resizable(False,False)

frame1=Frame(width=500,height=80)
frame1.pack(fill="both",expand=False)

frame2=Frame(width=500,height=80)
frame2.pack(fill="both",expand=False)

title=Label(frame1,text="게임",width="40",padx="10",pady="20",fg="blue",font="16")
title.grid(row=0,column=0)

btn_level_1=Button(frame2,text="1단계",width=10,height=5,command=lambda:show_monster(1))
btn_level_1.grid(row=0,column=0)

btn_level_2=Button(frame2,text="2단계",width=10,height=5,command=lambda:show_monster(2))
btn_level_2.grid(row=0,column=1)

window.mainloop()