from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("game")
window.geometry("500x300")

frame1 = Frame(window)
frame2 = Frame(window)

img=Image.open("C:\\Users\\thgh\\Documents\\프로그래밍1\\자료\\슬라임.jpg")
photo=ImageTk.PhotoImage(img)

hp1 = 50

def hpdown():
    global hp1
    hp1 = hp1 - 10
    hp.configure(text=str(hp1)+"/50")

frame2.pack_forget
frame1.pack(fill="both", expand=True)

monster=Button(frame1,image=photo,command=hpdown)
monster.pack()
hp = Label(frame1,text=str(hp1)+"/50",font=30)
hp.pack()

window.mainloop()