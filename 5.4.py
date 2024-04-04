# Определяем функцию для обработки списка оценок
def adjust_grades(grades):
    # Удаляем все двойки
    adjusted_grades = list(filter(lambda x: x != 2, grades))
    # Заменяем все тройки на четверки
    adjusted_grades = [4 if grade == 3 else grade for grade in adjusted_grades]
    return adjusted_grades

# Тестовые списки оценок
grades_lists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

# Обрабатываем каждый список оценок
for i, grades in enumerate(grades_lists, 1):
    adjusted_grades = adjust_grades(grades)
    print(f"Обновленный список оценок {i}: {adjusted_grades}")
