print("20224016-박소호")
import pygame.mixer

sounds=pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\heartbeat.wav")
wait_finish(s.play())

s2=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\buzz.wav")
wait_finish(s2.play())

s3=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\ohno.wav")
wait_finish(s3.play())

s4=sounds.Sound("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\sound\\carhorn.wav")
wait_finish(s4.play())
