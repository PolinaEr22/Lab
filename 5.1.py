# Данный список кодов работников, посетивших ресторан
cheque_codes = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 
                1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 
                5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 
                5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 
                3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

# Считаем количество выданных чеков, это же длина списка
total_cheques = len(cheque_codes)

# Считаем количество уникальных кодов работников, используя множество (set)
unique_visitors = len(set(cheque_codes))

# Находим самого частого посетителя
# Для этого создаем словарь, где ключ - это код работника, а значение - количество его посещений
visitors_frequency = {}
for code in cheque_codes:
    if code in visitors_frequency:
        visitors_frequency[code] += 1
    else:
        visitors_frequency[code] = 1

# Находим код работника с максимальным количеством посещений
most_frequent_visitor = max(visitors_frequency, key=visitors_frequency.get)
most_frequency = visitors_frequency[most_frequent_visitor]

# Выводим результат
print(f"Общее количество выданных чеков: {total_cheques}")
print(f"Количество разных людей, посетивших ресторан: {unique_visitors}")
print(f"Работник с кодом {most_frequent_visitor} посетил ресторан наибольшее количество раз - {most_frequency} раз(а)")

