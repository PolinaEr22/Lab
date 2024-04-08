def add_two_numbers():
    try:
        num1 = 2
        num2 = int(input("Введите число: "))
        result = num1 + num2
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Проведем тесты
add_two_numbers()
add_two_numbers()
