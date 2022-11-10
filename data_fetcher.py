import random
import time

def obdDataFetcher():
    gear = random.randint(0,5)
    speed = 0
    if gear == 1:
        speed = random.randint(0, 15)
    elif gear == 2:
        speed = random.randint(5,35)
    elif gear == 3:
        speed = random.randint(22,44)
    elif gear == 4:
        speed = random.randint(35,50)
    elif gear == 5:
        speed = random.randint(80,100)

    return gear, speed

while True:
    Gear, Speed = obdDataFetcher()
    print("Gear:" + str(Gear) + "  Speed: " + str(Speed))
    time.sleep(3)