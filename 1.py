def fib(n):
    a, b = 1, 1
    yield a
    yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b

# Генерируем и выводим первые 200 чисел Фибоначчи
for num, fibonacci_num in enumerate(fib(200), 1):
    print(f"Число Фибоначчи {num}: {fibonacci_num}")
