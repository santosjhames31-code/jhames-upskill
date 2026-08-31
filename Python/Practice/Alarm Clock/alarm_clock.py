
import datetime
import time as t
import pygame

def set_alarm(alarm_time):
    sound = "sound.mp3"
    print("-- Alarm Clock -- ")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Successfully set the alarm to {alarm_time}")
    
    while True:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        if time >= alarm_time:
            print("It's time!")
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(sound)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                t.sleep(0.2)

                while pygame.mixer.music.get_busy():
                    t.sleep(1)
            except pygame.error as e:
                print(f"Error : {e}")
            break
        t.sleep(1)

while True:
    try:    
        hours = int(input("Hour (1 - 24)    : "))
        minutes = int(input("Minute  (0 - 59) : "))
        seconds = int(input("Seconds (0 - 59) : "))
        if hours >= 0 and hours < 24 and minutes >= 0 and minutes < 60 and seconds >= 0 and seconds < 60:
            break
    except ValueError:
        print("Please enter an integer value")

set_alarm(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
