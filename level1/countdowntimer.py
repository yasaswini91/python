import time
t = int(input("enter the time in seconds:"))
for x in range(t,0,-1):
    seconds = x % 60
    minutes= int(x/60) % 60
    hour= int(x/3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
