print("20224016-박소호")
import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

sounds=pygame.mixer
sounds.init()

correct_s=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\correct.wav")
wrong_s=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\wrong.wav")

prompt="Press 1 for Correct, 2 for Wrong, or 0 to Quit:"

number_asked=0
number_correct=0
number_wrong=0

choice=input(prompt)
while choice !="0":
    if choice =='1':
        number_asked=number_asked+1
        number_correct=number_correct+1
        wait_finish(correct_s.play())
    if choice =='2':
        number_asked=number_asked+1
        number_wrong=number_wrong+1
        wait_finish(wrong_s.play())
    choice=input(prompt)

print("You asked" + str(number_asked)+"questions")
print(str(number_correct)+" were correctly answered")
print(str(number_wrong)+" were answered incorrectly")
