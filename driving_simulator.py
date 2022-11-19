class CarSimulator():

    def __init__(self, decelerationValue, model):
        self.speed = 0
        self.gear = 1
        self.deceleration = decelerationValue
        self.model = model

    def increaseSpeed(self):
        if str(int(self.speed + 1)) in self.model[str(self.gear)]:
            self.speed += 1

    def decreaseSpeed(self):
        if str(int(self.speed - 1)) in self.model[str(self.gear)]:
            self.speed -= 1

    def graduallySlow(self):
        if str(int(self.speed - self.deceleration)) in self.model[str(self.gear)]:
            self.speed -= self.deceleration

    def shiftUp(self):
        if str(self.gear + 1) in self.model:
            if str(int(self.speed)) in self.model[str(self.gear + 1)]:
                self.gear += 1

    def shiftDown(self):
        if str(self.gear - 1) in self.model:
            if str(int(self.speed)) in self.model[str(self.gear - 1)]:
                self.gear -= 1

    def update_car(self, control):
        if control != None:
            if control == 1:
                self.increaseSpeed()
            elif control == 2:
                self.decreaseSpeed()
            elif control == 3:
                self.shiftUp()
            elif control == 4:
                self.shiftDown()
        self.graduallySlow()

    def get_metrics(self):

        if str(int(self.speed)) in self.model[str(self.gear)]:
            FCR = self.model[str(self.gear)][str(int(self.speed))]
            return int(self.gear), int(self.speed), FCR
        else:
            return 0, 0, 0

