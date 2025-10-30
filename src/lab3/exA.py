import re

print("Тесты normalize")

def normalize(text, *, casefold = True, yo2e = True):
    text = re.sub(r"[\t\r\n\f\v]", " ", text)
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = re.sub(r" +", " ", text)
    return text.strip()

tests = ["ПрИвЕт\nМИр\t", "ёжик, Ёлка", "Hello\r\nWorld", "  двойные   пробелы  "]
for array in tests:
    result = normalize(array)
    print(f"{array} - {result}")

print("\n")
print("Тесты tokenize")

def tokenize(text):
    clear_text = re.sub(r'[^\w\s-]', ' ', text)
    new_text = clear_text.split()
    return new_text
tests = ["привет мир", "hello,world!!!", "по-настоящему круто", "2025 год", "emoji 😀 не слово"]
for array in tests:
    result = tokenize(array)
    print(f"{array} - {result}")


def count_freq(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq


print("\n")
print("Тесты count_freq и top_n")


def top_n(freq, n = 2):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

tests = [["a", "b", "a", "c", "b", "a"], ["bb", "aa", "bb", "aa", "cc"]]

for array in tests:
    result = top_n(count_freq((array)))
    print(f"{array} - {result}")
