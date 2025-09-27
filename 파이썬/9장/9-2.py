from tkinter import*
import pygame.mixer

app=Tk()
app.title("Head First Mix")
app.geometry("250x100+200+100")
sound_file=("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\mix_sound\\50459_M_RED_Nephlimizer.wav")
mixer=pygame.mixer
mixer.init()

def track_toggle():
    if track_playing.get()==1:
        track.play(loops=-1)
    else:
        track.stop()
def shutdown():
    track.stop()
    app.destroy()
    
track=mixer.Sound(sound_file)

track_playing=IntVar()
track_button=Checkbutton(app,variable=track_playing,command=track_toggle,text=sound_file)
track_button.pack()

app.protocol("WM_DELETE_WINDOW",shutdown)

app.mainloop()
