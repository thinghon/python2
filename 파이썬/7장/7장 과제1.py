print("20224016-박소호")
from tkinter import *
from unittest import TextTestResult
import pygame.mixer

def play_kill_sound():
    num_kill.set(num_kill.get() + 1)
    correct_s.play()
def play_assist_sound():
    num_assist.set(num_assist.get() + 1)
    correct_s.play()
def play_wrong_sound():
    num_dead.set(num_dead.get() + 1)
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry("600x250+300+200")

sounds = pygame.mixer
sounds.init()
correct_s = sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\correct.wav")
wrong_s = sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\wrong.wav")

num_kill = IntVar()
num_kill.set(0)
num_assist = IntVar()
num_assist.set(0)
num_dead = IntVar()
num_dead.set(0)

lab = Label(app, text = 'When you are ready, click on the buttons!', height = 3)

lab.pack()

lab1 = Label(app, textvariable = num_kill)
lab1.pack(side = 'left')

lab2 = Label(app,textvariable = num_assist)
lab2.pack(side='bottom')

lab3 = Label(app,textvariable = num_dead)
lab3.pack(side = 'right')

b1 = Button(app, text = "킬", width = 10, command = play_kill_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "어시스트", width = 10, command = play_assist_sound)
b2.pack(side = 'bottom', padx = 10, pady =10)

b3 = Button(app, text = "데스!", width = 10, command = play_wrong_sound)
b3.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()