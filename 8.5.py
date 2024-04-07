class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Автомобиль движется по дороге")

class Bus(Vehicle):
    def drive(self):
        print("Автобус перевозит пассажиров")

class Bicycle(Vehicle):
    def drive(self):
        print("Велосипед катится по дороге")


vehicles = [Car("Toyota", "Синий"), Bus("Volvo", "Белый"), Bicycle("Школьный", "Красный")]


for vehicle in vehicles:
    print(f"{vehicle.brand} {vehicle.color}:")
    vehicle.drive()
    print()
