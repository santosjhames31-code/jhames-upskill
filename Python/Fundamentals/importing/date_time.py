import datetime

date = datetime.date(1997, 12, 21)
today = datetime.date.today()
time = datetime.datetime.now()

time = time.strftime("%H:%M:%S | %m-%d-%Y")

print(today)
print(time)