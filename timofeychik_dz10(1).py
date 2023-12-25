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

car = Auto("BMW", 5, "blue", "X5", 1500)
car.move()  
car.stop()  "
car.birthday()
print(car.age)  