from tkinter import*
import tkinter.messagebox as mb
from tkinter import filedialog as fd

def callback():
    name=fd.askopenfilename()
    mb.showinfo("오픈파일 이름",name)

app = Tk()
app.title("오픈파일 테스트")
app.geometry('300x50+200+100')
Button(app, text='파일오픈', command=callback).pack(side='bottom')
app.mainloop()