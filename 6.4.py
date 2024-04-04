def find_sequence_between_ids(input_tuple, target_id):
    try:
        # Поиск первого индекса целевого элемента
        start_index = input_tuple.index(target_id)
    except ValueError:
        # Если элемент не найден, возвращаем пустой кортеж
        return ()
    
    try:
        # Поиск второго индекса целевого элемента
        # Начинаем поиск со следующей позиции после первого индекса
        end_index = input_tuple.index(target_id, start_index + 1)
        # Возвращаем срез с первого до второго индекса включительно
        return input_tuple[start_index:end_index + 1]
    except ValueError:
        # Если второй раз элемент не найден, возвращаем срез с первого индекса до конца
        return input_tuple[start_index:]

# Тесты функции
print(find_sequence_between_ids((1, 2, 3), 8))  # Ожидается: ()
print(find_sequence_between_ids((1, 8, 3, 4, 8, 8, 9, 2), 8))  # Ожидается: (8, 3, 4, 8)
print(find_sequence_between_ids((1, 2, 8, 5, 1, 2, 9), 8))  # Ожидается: (8, 5, 1, 2, 9)
