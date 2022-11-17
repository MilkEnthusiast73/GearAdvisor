import keyboard
from driving_simulator import*
import multiprocessing as mp
import os
import time
from communicate_with_database import *

feederDict = json_to_dict("FCRModelFeed.json")
car = CarSimulator(0.75,6,feederDict)

def check_for_input():
    print("hello")
    while True:
        if keyboard.is_pressed('up'):
            car.increaseSpeed()
            print("speed up")
        elif keyboard.is_pressed('down'):
            car.decreaseSpeed()
            print("speed down")
        elif keyboard.is_pressed('a'):
            car.shiftDown()
        elif keyboard.is_pressed('d'):
            car.shiftUp()
        time.sleep(0.5)

if __name__ == '__main__':
    p = mp.Process(target=check_for_input)
    p.start()
while True:
    #print(car.get_metrics())
    time.sleep(0.5)