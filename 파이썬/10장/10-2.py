from tkinter import*
from sound_panel import*
import pygame.mixer
import os
#박소호-20224016
app=Tk()
app.title("Head First Mix")
mixer=pygame.mixer
mixer.init()

os.chdir("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\mix_sound")
dirlList=os.listdir(".")
for fname in dirlList:
    if fname.endswith(".wav"):
        panel=SoundPanel(app,mixer,fname)
        panel.pack()

def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW",shutdown)

app.mainloop()