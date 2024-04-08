try:
    with open('empty_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("Файл пустой")
        else:
            print(f"Информация из файла 'empty_file.txt': {data}")
except Exception as e:
    print(e)

print("------")

try:
    with open('data_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("Файл пустой")
        else:
            print(f"Информация из файла 'data_file.txt': {data}")
except Exception as e:
    print(e)
