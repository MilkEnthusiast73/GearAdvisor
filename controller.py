from communicate_with_database import*
from interface import*
from shift_points_map import*
from plottingFCR import*
from driving_simulator import*
import time
import threading
from threading import Thread
import keyboard
import pygame
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

feederDict = json_to_dict("FCRModelFeed.json")
car = CarSimulator(0.01,5,feederDict)
view = Interface()
     
while True:
    control = view.check_for_input()
    car.update_car(control)
    gear, speed, FCR = car.get_metrics()
    direction = "NA"
    idealGear = 1
    if speed >= 1:
        direction = fetchAdvice(speed, gear)
        #print("Gear: "+str(idealGear)+" Direction: "+str(direction))
        update_plot("FCRModel.json", gear, speed, FCR)
    view.update_advice(direction, gear, speed, FCR)
    view.main_draw()
    view.clock.tick(60) #sets clock to 60 FPS 
