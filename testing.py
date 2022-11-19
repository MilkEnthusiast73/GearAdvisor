from driving_simulator import*
from communicate_with_database import *
import unittest
import random

class TestCarSim(unittest.TestCase):
    def test_increase_speed(self):
        feederDict = json_to_dict("FCRModel.json")
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


    # def test_get_metrics(self):
    #     feederDict = json_to_dict("FCRModel.json")
    #     testCar = CarSimulator(0.01,feederDict)
    #     gearNumber = random.randint(1,6)
    #     testCar.gear = feederDict[str(gearNumber)]
    #     testCar.speed = feederDict[]

    #     testCar.FCR = dee
    #     gear, speed, FCR = testCar.get_metrics()

if __name__ == '__main__':
    unittest.main()