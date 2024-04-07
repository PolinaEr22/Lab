class Car:
    def __init__(self, brand, color, year):
        self._brand = brand
        self._color = color
        self._year = year
        self._mileage = 0
    
    def display_info(self):
        print(f"Марка: {self.get_brand()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Год выпуска: {self.get_year()}")
        print(f"Пробег: {self.get_mileage()} км")
    
    def get_brand(self):
        return self._brand
    
    def get_color(self):
        return self._color
    
    def get_year(self):
        return self._year
    
    def get_mileage(self):
        return self._mileage
    
    def set_color(self, new_color):
        print(f"Изменяем цвет с {self._color} на {new_color}")
        self._color = new_color
    
    def add_mileage(self, distance):
        print(f"Проехали {distance} км")
        self._mileage += distance

# Создаем объект класса Car
my_car = Car("Toyota", "Синий", 2020)

# Выводим информацию об автомобиле
my_car.display_info()

# Изменяем цвет автомобиля
my_car.set_color("Красный")

# Осуществляем поездку и увеличиваем пробег
my_car.add_mileage(150)
my_car.display_info()
