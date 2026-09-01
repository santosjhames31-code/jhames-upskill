import time

seconds = int(input("Enter seconds : "))

for i in range(seconds, 0, -1):
    seconds = i % 60
    mins = int(i / 60)
    hours = int(mins / 60)
    time.sleep(1)
    print(f"{hours:02}:{mins:02}:{seconds:02}")
