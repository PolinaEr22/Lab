
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.mileage = 0
    
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Цвет: {self.color}")
        print(f"Год выпуска: {self.year}")
        print(f"Пробег: {self.mileage} км")
    
    def drive(self, distance):
        self.mileage += distance
        print(f"Проехали {distance} км")

class HybridCar(Car):
    def __init__(self, brand, color, year, fuel_tank_capacity):
        super().__init__(brand, color, year)
        self.fuel_tank_capacity = fuel_tank_capacity
    
    def drive(self, distance):
        fuel_consumed = distance * 0.05
        if fuel_consumed <= self.fuel_tank_capacity:
            super().drive(distance)
            self.fuel_tank_capacity -= fuel_consumed
            print(f"Остаток топлива в бензобаке: {self.fuel_tank_capacity} л")
        else:
            print("Недостаточно топлива для поездки!")


my_hybrid_car = HybridCar("Toyota", "Зеленый", 2022, 40)

my_hybrid_car.display_info()

my_hybrid_car.drive(75)
