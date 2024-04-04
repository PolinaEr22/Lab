def find_top_three_numbers(input_string):
    # Создаем словарь для подсчета каждого числа
    count_dict = {}
    for num in input_string:
        # Увеличение счетчика для текущего числа
        # Преобразовываем строку в число для использования в качестве ключа
        num = int(num)  
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Сортируем словарь по количеству повторений и извлекаем 3 наиболее частых числа
    top_three = sorted(count_dict, key=lambda x: (-count_dict[x], x))[:3]
    
    # Создаем новый словарь из 3 самых частых чисел
    # Отсортируем ключи (числа) по возрастанию
    result_dict = {num: count_dict[num] for num in sorted(top_three)}
    
    return result_dict

# Пример использования функции
input_string = "123213545657689090987654321"
result = find_top_three_numbers(input_string)
print(result)
