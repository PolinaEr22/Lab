def remove_first_occurrence_from_tuple(tpl, value):
    # Проверяем, существует ли элемент в кортеже
    if value in tpl:
        # Находим индекс первого появления элемента
        index = tpl.index(value)
        # Возвращаем новый кортеж без этого элемента
        return tpl[:index] + tpl[index+1:]
    else:
        # Если элемента нет в кортеже, возвращаем исходный кортеж
        return tpl

# Тестирование функции
tuple1 = (1, 2, 3)
print(remove_first_occurrence_from_tuple(tuple1, 1)) # Ожидаемый результат: (2, 3)

tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
print(remove_first_occurrence_from_tuple(tuple2, 3)) # Ожидаемый результат: (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)

tuple3 = (2, 4, 6, 6, 4, 2)
print(remove_first_occurrence_from_tuple(tuple3, 9)) # Ожидаемый результат: (2, 4, 6, 6, 4, 2)
