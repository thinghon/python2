from tkinter import*
import pygame.mixer
import tkinter.messagebox as mb
from tkinter import filedialog as fd

a=0

def callback():
    global track,name
    name=fd.askopenfilename()
    sound_file=(name)
    mixer=pygame.mixer
    mixer.init()
    track=mixer.Sound(sound_file)
    change()
    return name

def change():
    global name,a
    a+=1
    if a > 1:
        label.configure(text=name)
        
app=Tk()
app.title("Head First Mix")
app.geometry("300x100+200+100")
Button(app, text='파일오픈', command=callback).pack(side='bottom')

mixer=pygame.mixer
mixer.init()

def track_start():
    track.play(loops=-1)
def track_stop():
    track.stop()
def shutdown():
    track.stop()
    app.destroy()

track=mixer.Sound(callback())

start_button=Button(app,command=track_start,text="start")
start_button.pack(side=LEFT)

stop_button=Button(app,command=track_stop,text="stop")
stop_button.pack(side=RIGHT)

label = Label(app,text=name)
label.pack(side='top')

app.protocol("WM_DELETE_WINDOW",shutdown)

app.mainloop()
