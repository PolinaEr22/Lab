def generate_set_from_list(input_list):
    # Считаем количество каждого элемента в списке
    element_count = {}
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
            
    # Создаем множество с уникальными элементами и строками для повторяющихся элементов
    result_set = set()
    for element, count in element_count.items():
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(element)
            else:
                result_set.add(str(element) * i)
                
    return result_set

# Тестовые списки
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

# Генерируем и выводим множества
set_1 = generate_set_from_list(list_1)
set_2 = generate_set_from_list(list_2)
set_3 = generate_set_from_list(list_3)

print(set_1)
print(set_2)
print(set_3)
