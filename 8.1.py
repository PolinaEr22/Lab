class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Цвет: {self.color}")
        print(f"Год выпуска: {self.year}")

my_car = Car("Toyota", "Синий", 2020)

my_car.display_info()
