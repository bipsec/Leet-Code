class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True
        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True
        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2] -= 1
                return True
        return False


obj = ParkingSystem(1, 1, 0)
# [1, 1, 0], [1], [2], [3], [1]
param_1 = obj.addCar([1, 1, 0])
param_2 = obj.addCar(1)
param_3 = obj.addCar(2)
param_4 = obj.addCar(3)
param_5 = obj.addCar(1)

print(param_1, param_2, param_3, param_4, param_5)
