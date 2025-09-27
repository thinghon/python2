from tkinter import*
from sound_panel import*
import pygame.mixer
#박소호-20224016
app = Tk()
app.title("Head First Mix")
mixer=pygame.mixer
mixer.init()

panel=SoundPanel(app,mixer,"C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\mix_sound\\50459_M_RED_Nephlimizer.wav")
panel.pack()
panel=SoundPanel(app, mixer,"C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\mix_sound\\49119_M_RED_HardBouncer.wav")
panel.pack()

def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()