from shift_points_map import *
from plottingFCR import*
#from interface import*
from communicate_with_database import *
import unittest
import random
import pygame
from pygame import tests as pTests

class TestShiftMap(unittest.TestCase):

    def test_find_shift_points(self):
        knownShiftPoints = [0, 7, 29, 37, 40, 56]
        dictionary = json_to_dict("FCRModelFeed.json")
        newShiftPoints = find_shift_points(dictionary)
        self.assertEqual(knownShiftPoints,newShiftPoints)

    def test_fetch_advice(self):
        Dict = json_to_dict("FCRModel.json")
        shiftpoints = [0, 7, 29, 37, 40, 56]
        for gear, shiftpointIndex in zip(Dict,range(0,len(shiftpoints))):
            if int(gear)<6:
                shiftpoint = shiftpoints[shiftpointIndex+1]
                for speed in Dict[str(int(gear)+1)]:
                    advice = fetchAdvice(int(speed), int(gear))
                    if int(speed) < shiftpoint:
                        self.assertEqual(advice,"maintain")
                    else:
                        self.assertEqual(advice,"up")

class TestPlotting(unittest.TestCase):

    def test_updatePlot(self):
        Dictionary1 = {}
        fileName1 = "Test.json"     #start with two identical json files
        fileName2 = "Test2.json"
        dict_to_json(Dictionary1, fileName1)
        dict_to_json(Dictionary1, fileName2)
        

        Dictionary1 = json_to_dict(fileName1)
        
        for number in range(1,100):    
            #create variables to be added to the dictionaries
            currentGear = random.randint(1,7)
            currentSpeed = random.randint(0,160)
            currentFCR = random.randint(0,18)


            #write to one json using the Update plot function
            update_plot(fileName2, currentGear, currentSpeed, currentFCR)
            #write to a dictionary using these variables
            if str(currentGear) not in Dictionary1:
                Dictionary1[str(currentGear)] = {}
            Dictionary1[str(currentGear)][str(currentSpeed)] = currentFCR
            
            #convert json to dictionary        
            Dictionary2 = json_to_dict(fileName2)
            
            #compare dictionaries
            self.assertEqual(Dictionary1,Dictionary2)