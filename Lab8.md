# Тема 8. Введение в ООП
Отчет по Теме №8 выполнил(а):
- Еремеева Полина Алексеевна
- ИНО ЗБ ПОАС 22-1

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 |  + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1

## Самостоятельно создайте класс и его объект. 

```python
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
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема8/pic/1.png)

## Выводы

В данном коде создается класс Car, который содержит атрибуты brand, color и year, и метод display_info, который выводит информацию о марке, цвете и годе выпуска автомобиля. 
После определения класса Car, создается объект my_car этого класса с атрибутами "Toyota", "Синий", 2020. Затем вызывается метод display_info() объекта my_car, который выводит информацию о марке, цвете и годе выпуска этого автомобиля.

## Самостоятельная работа №2

## Самостоятельно создайте атрибуты и методы для ранее созданного класса.

```python
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
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема8/pic/2.png)

## Выводы

В данном коде определен класс Car, который имеет атрибуты brand, color, year и mileage, а также методы display_info, drive, и show_mileage.

1. Метод display_info(self) - Этот метод выводит информацию о марке, цвете, годе выпуска и пробеге автомобиля.
2. Метод drive(self, distance) - Этот метод увеличивает пробег автомобиля на указанное расстояние distance и выводит сообщение о пройденном расстоянии.
3. Метод show_mileage(self) - Этот метод выводит текущий пробег автомобиля.

После определения класса Car, создается объект my_car этого класса с атрибутами "Toyota", "Синий", 2020. Затем вызывается метод display_info(), который выводит информацию о марке, цвете, годе выпуска и пробеге автомобиля. Затем вызывается метод drive(100), который увеличивает пробег на 100 км, и затем вызывается метод show_mileage(), который выводит текущий пробег автомобиля.

## Самостоятельная работа №3

## 
```python
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
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема8/pic/3.png)

## Выводы

В данном коде определены два класса: Car и HybridCar, где HybridCar является подклассом Car.

Класс Car содержит атрибуты brand, color, year, mileage, метод display_info для отображения информации о автомобиле и метод drive для увеличения пробега автомобиля и вывода информации о пройденном расстоянии.

Класс HybridCar наследует от класса Car и добавляет новый атрибут fuel_tank_capacity (емкость топливного бака) и переопределяет метод drive для учета расхода топлива.

После создания объекта my_hybrid_car класса HybridCar с атрибутами "Toyota", "Зеленый", 2022 и емкостью бензобака 40 литров, вызывается метод display_info(), который отображает информацию о машине. Затем вызывается метод drive(75), который пытается проехать 75 км, учитывая расход топлива.

## Самостоятельная работа №4

## Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом.

```python
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


my_car = Car("Toyota", "Синий", 2020)

my_car.display_info()

my_car.set_color("Красный")

my_car.add_mileage(150)
my_car.display_info()
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема8/pic/4.png)

## Выводы

В данном коде определен класс Car, который имеет атрибуты _brand, _color, _year, _mileage, а также методы display_info, get_brand, get_color, get_year, get_mileage, set_color, add_mileage.

- Метод display_info(self) выводит информацию о марке, цвете, годе выпуска и пробеге автомобиля, используя методы для доступа к атрибутам.
- Методы get_brand, get_color, get_year, get_mileage возвращают соответствующие значения атрибутов.
- Метод set_color(self, new_color) изменяет цвет автомобиля, выводит сообщение об изменении цвета и обновляет значение атрибута _color.
- Метод add_mileage(self, distance) увеличивает пробег автомобиля на указанное расстояние и выводит сообщение о пройденном расстоянии.

Создается объект my_car класса Car с атрибутами "Toyota", "Синий", 2020. Затем вызывается метод display_info(), который выводит информацию о марке, цвете, годе выпуска и пробеге автомобиля. Затем вызывается метод set_color("Красный"), который изменяет цвет автомобиля на "Красный" и выводит сообщение об изменении цвета. После этого вызывается метод add_mileage(150), который увеличивает пробег на 150 км. Наконец, вызывается метод display_info(), чтобы отобразить обновленную информацию об автомобиле.

## Самостоятельная работа №5

## Самостоятельно реализуйте полиморфизм.

```python
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
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема8/pic/5.png)

## Выводы

В данном коде определены классы Vehicle, Car, Bus, Bicycle, все унаследованы от класса Vehicle и переопределяют метод drive().

- Vehicle содержит атрибуты brand и color, и определяет метод drive(), который пока не выполняет никаких действий (просто имеет оператор pass).
- Car, Bus и Bicycle - это подклассы класса Vehicle, они переопределяют метод drive() и выводят соответствующие сообщения о движении для автомобиля, автобуса и велосипеда соответственно.

Затем создается список vehicles, который содержит объекты разных типов: Car, Bus, Bicycle, каждый с определенным брендом и цветом. 

Далее, в цикле проходим по каждому элементу vehicle в списке vehicles, выводим информацию о бренде и цвете транспортного средства, вызываем метод drive() соответствующего класса для каждого элемента, чтобы вывести сообщение о движении.
