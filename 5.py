# Создание собственного исключения CustomException
class CustomException(Exception):
    def __init__(self, message="Сработало наше собственное исключение!"):
        self.message = message
        super().__init__(self.message)

# Пример использования исключения в первом фрагменте кода
try:
    raise CustomException("Пример использования исключения в первом фрагменте кода")
except CustomException as e:
    print(f"Первый фрагмент кода: {e}")

# Пример использования исключения во втором фрагменте кода
def important_function(value):
    if value < 0:
        raise CustomException("Значение не может быть отрицательным")
    return value

try:
    result = important_function(-5)
    print(f"Второй фрагмент кода: Результат функции: {result}")
except CustomException as e:
    print(f"Второй фрагмент кода: {e}")
