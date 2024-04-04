import math

# Заданные списки длин сторон
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

# Находим максимальные значения
max_a = max(one)
max_b = max(two)
max_c = max(three)

# Находим минимальные значения
min_a = min(one)
min_b = min(two)
min_c = min(three)

# Функция для расчета площади треугольника по формуле Герона
def heron_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Рассчитываем площади
max_area = heron_area(max_a, max_b, max_c)
min_area = heron_area(min_a, min_b, min_c)

print("Площадь треугольника, составленная из максимальных элементов:", max_area)
print("Площадь треугольника, составленная из минимальных элементов:", min_area)
