class Vehicle:
    def __init__(self, name, color, model, engine):
        self.name = name
        self.color = color
        self.model = model
        self.engine = engine

    def __str__(self):
        return "This is a Brand New Car!"

    def capacity(self, amount):
        return "The {} has capacity of around {} people".format(self.name, amount)


class Car(Vehicle):
    def __init__(self, name, color, model, engine):
        super().__init__(name, color, model,engine)

    def move(self, val):
        return "The {} moves ata speed of {}km/hour".format(self.name, val)

    def hold(self):
        print("{} has Good Break Quality!".format(self.name))


class Bus(Vehicle):
    def __init__(self, size, color, model, engine):
        super().__init__(size, color, model, engine)

    def move(self, val):
        return "The {} moves ata speed of {}km/hour".format(self.name, val)

    def hold(self):
        print("{} has Superb Break Quality!".format(self.name))


class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level

    def __str__(self):
        return ("\n \tFuel: " + str(self.fuel_type)) + \
               ("\n \tNoiseLevel: " + str(self.noise_level))


def can_break(vehicle):
    vehicle.hold()


print("---------CAR DETAILS:---------")
audi_engine = Engine("Disel", "Moderate")
audi = Car("AUDI", "Black", "MK5001C", audi_engine)
print("Car Name: ", audi.name)
print("Car Color: ", audi.color)
print("Car Model: ", audi.model)
print("Car Speed: ", audi.move(50))
print("Car Capacity: ", audi.capacity(4))
print("Car Engine: ", audi.engine)
print()
print("---------BUS DETAILS:---------")
ena_engine = Engine("Petrol", "High")
ena = Bus("HUNDAI", "Red", "MK50901C", ena_engine)
print("Bus Name: ", ena.name)
print("Bus Color: ", ena.color)
print("Bus Model: ", ena.model)
print("Bus Speed: ", ena.move(150))
print("Bus Capacity: ", ena.capacity(40))
print("Bus Engine: ", ena.engine)

can_break(audi)
can_break(ena)












class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def __str__(self):
        return "{} is the future of a nation".format(self.name)


class Name(Student):
    def __init__(self, section, form, name, roll, dept):
        super().__init__(name, roll, dept)
        self.section = section
        self.form = form

    def hight(self, h):
        return "{} has a hight of {}".format(self.name, h)


# bappy = Name("A", "Meritorious", "Bappy", 20123713, "CSE")
# print(bappy.name)
# print(bappy.roll)
# print(bappy.dept)
# print(bappy.hight(20))
# print(bappy)
