import keyboard

class CarSimulator():

    def __init__(self, decelerationValue, gearCount, model):
        self.speed = 0
        self.gear = 1
        self.deceleration = decelerationValue
        self.maxGear = gearCount
        self.model = model

    def increaseSpeed(self):
        if str(self.speed + 1) in self.model[str(self.gear)]:
            self.speed += 1

    def decreaseSpeed(self):
        if str(self.speed - 1) in self.model[str(self.gear)]:
            self.speed -= 1

    def graduallySlow(self):
        self.speed -= self.deceleration

    def shiftUp(self):
        if self.gear < self.gearCount:
            self.gear += 1

    def shiftDown(self):
        if self.gear > 1:
            self.gear -= 1

    def get_metrics(self):
        if self.speed in self.model[str(self.gear)]:
            FCR = self.model[str(self.gear)][str(int(self.speed))]
            return int(self.gear), int(self.speed), FCR
        else:
            return 0, 0, 0

