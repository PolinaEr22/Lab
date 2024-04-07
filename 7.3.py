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
