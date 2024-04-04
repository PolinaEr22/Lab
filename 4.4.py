def average(*args):
    if len(args) == 0:
        print("Нет аргументов для вычисления среднего")
        return

    total = sum(args)
    avg = total / len(args)
    print(f"Среднее арифметическое: {avg}")

if __name__ == "__main__":
    nums = [float(num) for num in input("Введите числа через пробел: ").split()]
    average(*nums)
