from driving_simulator import *
from communicate_with_database import *
from shift_points_map import *
from plottingFCR import*
import unittest
import random

class TestCarSim(unittest.TestCase):

    def test_increase_speed(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)

        for gear in feederDict:
            testCar.gear = int(gear)
            
            list_of_speeds = []
             
            for speed in feederDict[gear]:
                list_of_speeds.append(int(speed))

            # we will call increase speed ---- it should increase speed
            for Speed in list_of_speeds[0:-1]:
                originalSpeed = Speed
                testCar.speed = originalSpeed
                testCar.increaseSpeed()
                newSpeed = testCar.speed
                self.assertLess(originalSpeed, newSpeed)
            
            #we will call increase speed ---- it should not have increased
            originalSpeed = list_of_speeds[len(list_of_speeds)-1]
            testCar.speed = originalSpeed
            testCar.increaseSpeed()
            newSpeed = testCar.speed
            self.assertEqual(originalSpeed, newSpeed)

    def test_decr_speed(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)

        for gear in feederDict:
            testCar.gear = int(gear)
            list_of_speeds = []

            for speed in feederDict[gear]:
                list_of_speeds.append(int(speed))

            for Speed in list_of_speeds[1:len(list_of_speeds)-1]:
                originalSpeed = Speed
                testCar.speed = originalSpeed
                testCar.decreaseSpeed()
                newSpeed = testCar.speed
                self.assertGreater(originalSpeed, newSpeed)

            originalSpeed = list_of_speeds[0]
            testCar.speed = originalSpeed
            testCar.decreaseSpeed()
            newSpeed = testCar.speed
            self.assertEqual(originalSpeed, newSpeed)

    def test_gradually_slow(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)

        for gear in feederDict:
            testCar.gear = int(gear)
            list_of_speeds = []

            for speed in feederDict[gear]:
                list_of_speeds.append(int(speed))

            for Speed in list_of_speeds[1:len(list_of_speeds)-1]:
                originalSpeed = Speed
                testCar.speed = originalSpeed
                testCar.graduallySlow()
                newSpeed = testCar.speed
                self.assertGreater(originalSpeed, newSpeed)

            originalSpeed = list_of_speeds[0]
            testCar.speed = originalSpeed
            testCar.graduallySlow()
            newSpeed = testCar.speed
            self.assertEqual(originalSpeed, newSpeed)

    def test_shift_up(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)

        maxGear = 0
        maxSpeed = 0
        for gear in feederDict:
            maxGear = int(gear)
            for speed in feederDict[gear]:
                maxSpeed = int(speed)

        while True:
            if testCar.speed == maxSpeed and testCar.gear == maxGear:
                break
            orginalGear = testCar.gear
            testCar.increaseSpeed()
            advice = fetchAdvice(testCar.speed, testCar.gear)
            if advice == 'up':
                testCar.shiftUp()
                newGear = testCar.gear
                self.assertLess(orginalGear, newGear)


    def test_shift_down(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)
        
        maxGear = 0
        maxSpeed = 0
        for gear in feederDict:
            maxGear = int(gear)
            for speed in feederDict[gear]:
                maxSpeed = int(speed)
        
        testCar.speed = maxSpeed
        testCar.gear = maxGear
        minGear = 1
        minSpeed = 0

        while True:
            if testCar.speed == minSpeed and testCar.gear == minGear:
                break
            orginalGear = testCar.gear
            oldSpeed = testCar.speed
            testCar.decreaseSpeed()
            newSpeed = testCar.speed
            if newSpeed == oldSpeed:
                testCar.shiftDown()
                newGear = testCar.gear
                self.assertGreater(orginalGear, newGear)

    def test_update_car(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)
        controls = [None, 1,2,3,4]
        # test to see if first if control == 1 is called
        minMax_per_gear = {}
        maxGear = 0
        for gear in feederDict:
            minMax_per_gear[gear] = []
            maxGear = int(gear)
            for speed in feederDict[gear]:
                minMax_per_gear[gear].append(int(speed))
                break
            for speed in feederDict[gear]:
                maxSpeed = int(speed)
            minMax_per_gear[gear].append(maxSpeed)


        for gear in feederDict:
            min_and_max = minMax_per_gear[gear]

            for speed in feederDict[gear]:
                testCar.speed = int(speed)
                testCar.gear = int(gear)

                for control in controls:
                    org_speed = testCar.speed
                    org_gear = testCar.gear
                    advice = fetchAdvice(testCar.speed, testCar.gear)
                    testCar.update_car(control)
                    newSpeed = testCar.speed

                    if control == 1 and int(speed) != min_and_max[1]:
                        newspeed = testCar.speed
                        self.assertLess(org_speed, newspeed )

                    elif control == 2 and int(speed) != min_and_max[0]:
                        newspeed = testCar.speed
                        self.assertGreater(org_speed, newspeed )
                        
                    elif control == 3 and int(gear) != maxGear and advice == 'up':
                        newgear = testCar.gear
                        self.assertLess(org_gear, newgear )
                        
                    elif control == 4 and int(gear) != 1 and testCar.speed == min_and_max[0]:
                        newgear = testCar.gear
                        self.assertGreater(org_gear, newgear)

    def test_get_metrics(self):
        feederDict = json_to_dict("FCRModelFeed.json")
        testCar = CarSimulator(0.01,feederDict)

        for gear in feederDict:
            testCar.gear = int(gear)
            for speed in feederDict[gear]:
                testCar.speed = int(speed)
                FCR = feederDict[gear][speed]
                tupleOfMetrics = int(gear), int(speed), FCR
                self.assertEqual(testCar.get_metrics(), tupleOfMetrics)

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


class TestReadWriteDataBase(unittest.TestCase):
    
    def test_readWrite_jsonAndDict(self):
        testDict = {"hello":"world"}
        testFileName = "test.json"
        dict_to_json(testDict, testFileName)

        returnDict = json_to_dict(testFileName)
        self.assertEqual(testDict, returnDict)