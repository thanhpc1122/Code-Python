import time

myTime = int(input("nhập vào số giây : "))

for i in range(myTime,0,-1):
    second = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
    if hours == 0 and minutes == 0 and second -1 == 0:
        print("00:00:00")
time.sleep(3)
