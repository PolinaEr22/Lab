# Тема 7. Работа с файлами (ввод, вывод) 
Отчет по Теме №7 выполнил(а):
- Еремеева Полина Алексеевна
- ИНО ЗБ ПОАС 22-1

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 |  - |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.


## Самостоятельная работа №2

## У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией 


```python
import json


def add_expense(expenses):
    category = input("Введите категорию расходов: ")
    amount = float(input("Введите сумму расходов: "))
    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("Расход успешно добавлен!")


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    return expenses


def show_expenses(expenses):
    for expense in expenses:
        print(f"Категория: {expense['category']}, Сумма: {expense['amount']}")


def main():
    expenses = load_expenses()

    while True:
        choice = input("Выберите действие: 1 - добавить расход, 2 - просмотреть расходы, 3 - выход: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Некорректный ввод, попробуйте еще раз.")


if __name__ == "__main__":
    main()
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема7/pic/2.png)

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема7/pic/2.1.png)

## Выводы
Данный код представляет собой программу для учета расходов. В ней определены функции:

1. add_expense(expenses): Данная функция добавляет новую запись о расходе в список expenses. Пользователю предлагается ввести категорию расходов и сумму расходов, после чего эти данные добавляются в список расходов.
   
2. save_expenses(expenses): Функция сохраняет список расходов в файл "expenses.json" в формате JSON. Таким образом, данные о расходах сохраняются для последующего использования.

3. load_expenses(): Данная функция загружает данные о расходах из файла "expenses.json" в случае, если файл существует, либо создает пустой список расходов.

4. show_expenses(expenses): Функция выводит на экран все записи о расходах, содержащиеся в списке expenses.

5. main(): Основная функция программы, в которой выполняется основной цикл работы. Пользователю предлагается выбрать действие: добавить расход, просмотреть список расходов или выйти из программы. В зависимости от выбора пользователя вызываются соответствующие функции.

## Самостоятельная работа №3

## Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.


```python
def count_statistics(filename):
    with open(filename, 'r') as file:
        text = file.read()
        letters = sum(char.isalpha() for char in text)
        words = len(text.split())
        lines = text.count('\n') + 1

    return letters, words, lines

filename = "input.txt"
letters, words, lines = count_statistics(filename)

print(f"Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines} lines")
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема7/pic/3.png)


## Выводы
Данный код открывает файл input.txt, считывает его содержимое, а затем с помощью методов str.isalpha(), str.split() и подсчета символов новой строки подсчитывает количество букв, слов и строк в тексте соответственно. Итоговая статистика выводится на экран.

## Самостоятельная работа №4

## Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре.

```python
def load_forbidden_words(filename):
    with open(filename, 'r') as file:
        forbidden_words = file.read().split()
    return forbidden_words


def get_forbidden_words(filename):
    with open(filename, 'r') as file:
        forbidden_words = file.read().split()
    return forbidden_words

def censor_sentence(sentence, forbidden_words):
    censored_sentence = sentence
    for forbidden_word in forbidden_words:
        lowercase_word = forbidden_word.lower()
        censored_word = '*' * len(forbidden_word)
        censored_sentence = censored_sentence.replace(lowercase_word, censored_word)
    return censored_sentence

filename = 'input.txt'
forbidden_words = get_forbidden_words(filename)

sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
censored_sentence = censor_sentence(sentence.lower(), forbidden_words)

print("Исходное предложение:")
print(sentence)
print("Предложение с замененными запрещенными словами:")
print(censored_sentence)
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема7/pic/4.png)

## Выводы
Данный код считывает запрещенные слова из файла input.txt, заменяет все вхождения этих слов на звездочки в предложении, игнорируя регистр, и выводит скорректированное предложение на экран.

## Самостоятельная работа №5

## Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
def count_emails(filename):
    with open(filename, 'r') as file:
        emails = file.readlines()
    return len(emails), emails

def most_common_domain(emails):
    domains = {}
    for email in emails:
        domain = email.split('@')[-1].strip()
        domains[domain] = domains.get(domain, 0) + 1
    most_common_domain = max(domains, key=domains.get)
    return most_common_domain, domains[most_common_domain]

filename = "emails.txt"
total_emails, all_emails = count_emails(filename)
print(f"Количество email адресов в файле: {total_emails}")

most_common_domain, num_users = most_common_domain(all_emails)
print(f"Наиболее часто встречающийся домен: {most_common_domain}, количество пользователей: {num_users}")
```
### Результат.

![Меню](https://github.com/PolinaEr22/Lab/blob/Тема7/pic/5.png)

## Выводы
Код программы считывает адреса из файла, находит общее количество адресов и наиболее часто встречающийся домен, выводит все это на экран.
