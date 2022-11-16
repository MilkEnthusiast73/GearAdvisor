from communicate_with_database import*
from interface import*
from shift_points_map import*
from plottingFCR import*
from driving_simulator import*
import time
import threading
from threading import Thread
import keyboard

feederDict = json_to_dict("FCRModelFeed.json")
view = Interface()
car = CarSimulator(0.75,6,feederDict)

def check_for_input():
    while True:

        if keyboard.is_pressed('K_UP'):
            car.increaseSpeed()
        elif keyboard.is_pressed('K_DOWN'):
             car.decreaseSpeed()
        elif keyboard.is_pressed('a'):
             car.shiftDown()
        elif keyboard.is_pressed('d'):
            car.shiftUp()
        time.sleep(1)

driveThread = Thread(target=check_for_input)
driveThread.start()
while True:
    gear, speed, FCR = car.get_metrics()
    direction = "NA"
    idealGear = 1
    if speed >= 1:
        direction, idealGear = fetchAdvice(speed, gear)
        update_plot("FCRModel.json", gear, speed, FCR)
    view.update_advice(direction, idealGear)
    view.draw()
