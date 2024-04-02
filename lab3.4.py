sentence = input("Введите предложение на английском: ")
print("Длина предложения:", len(sentence))
lower_sentence = sentence.lower()

print("Предложение в нижнем регистре:", lower_sentence)
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = sum([1 for char in lower_sentence if char in vowels])

print("Количество гласных букв в предложении:", count_vowels)
new_sentence = lower_sentence.replace("ugly", "beauty")
print("Предложение с заменой:", new_sentence)

if lower_sentence.startswith("the") and lower_sentence.endswith("end"):
    print("Предложение начинается с 'The' и заканчивается на 'end'")
else:
    print("Предложение не соответствует условиям")
