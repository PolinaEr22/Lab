# Создаем собственный декоратор
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Декоратор добавляет дополнительное поведение перед выполнением функции")
        result = func(*args, **kwargs)
        print("Декоратор добавляет дополнительное поведение после выполнения функции")
        return result
    return wrapper

# Применяем декоратор к двум выдуманным функциям
@my_decorator
def greet(name):
    return f"Привет, {name}"

@my_decorator
def square(n):
    return n ** 2

# Вызываем и тестируем функции с декоратором
print(greet("Вася"))
print(square(5))
