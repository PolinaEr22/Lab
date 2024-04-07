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
    
    def show_mileage(self):
        print(f"Пробег автомобиля: {self.mileage} км")


my_car = Car("Toyota", "Синий", 2020)

my_car.display_info()

my_car.drive(100)
my_car.show_mileage()
