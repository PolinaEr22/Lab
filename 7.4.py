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
