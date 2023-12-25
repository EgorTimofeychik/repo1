import time

class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Sedan(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")


truck1 = Truck("Volvo", 3, "red", "FH16", 5000, 10000)
truck2 = Truck("Scania", 5, "blue", "R500", 6000, 12000)

sedan1 = Sedan("Toyota", 2, "silver", "Camry", 1500, 200)
sedan2 = Sedan("Honda", 4, "black", "Civic", 1400, 180)

truck1.move()
truck1.load()
print(truck1.max_load)

sedan1.move()
print(sedan1.max_speed)
truck1 = Truck("Volvo", 3, "red", "FH16", 5000, 10000)
truck2 = Truck("Scania", 5, "blue", "R500", 6000, 12000)

sedan1 = Sedan("Toyota", 2, "silver", "Camry", 1500, 200)
sedan2 = Sedan("Honda", 4, "black", "Civic", 1400, 180)

truck1.move()
truck1.load()
print(truck1.max_load)

sedan1.move()
print(sedan1.max_speed)
