# Получаем строку чисел, разделенных пробелами, от пользователя
user_input = input("Введите числа, разделенные пробелом: ")

# Преобразуем введённую строку в список, где каждый элемент - это число
# Для этого сначала используем метод split(), чтобы разделить строку по пробелам, получая список строк
# Затем применяем list comprehension, чтобы преобразовать каждый элемент списка из строки в число
numbers_list = [int(number) for number in user_input.split()]

# Преобразуем список чисел в кортеж
numbers_tuple = tuple(numbers_list)

# Выводим полученный список и кортеж
print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)
