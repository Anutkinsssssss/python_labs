# Лабораторна работа №1

Задача 1
```py
name = input()
age = int(input())
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```
![Привет и возраст](./images/lab1/img_1.png)

Задача 2
```py
import math
a1 = input()
a2 = input()
a1 = a1.replace(',', '.')
a2 = a2.replace(',', '.')
a1 = float(a1)
a2 = float(a2)
sum = a1 + a2
avg = sum / 2
print(f'sum={sum}; avg={round(avg, 2)}')
```
![Сумма и среднее](/images/lab1/img_2.png)

Задача 3
```py
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}')
print(f'НДС:               {vat_amount:.2f}')
print(f'Итого к оплате:    {total:.2f}')
```
![Чек: скидка и НДС](/images/lab1/img_3.png)

Задача 4
```py
m = int(input())
ch = m // 60
print(f'{ch}:{m - ch * 60}')
```
![Минуты -> ЧЧ:ММ](/images/lab1/img_4.png)

Задача 5
```py
fio = input().split()
print(f'Инициалы: {fio[0][0] + fio[1][0] + fio[2][0]}.')
print(f'Длина (символов): {len(fio[0]) + len(fio[1]) + len(fio[2]) + 2}')
```
![Инициалы и длина строки](/images/lab1/img_5.png)

Задача 6
```py
n = int(input().strip())
t = 0
f = 0
for x in range(n):
    line = input().strip()
    a = line.split()
    b = a[-1]
    if b == 'True':
        t += 1
    elif b == 'False':
        f += 1
print(t, f)
```
![Задание со звёздочкой](/images/lab1/img_6.png)

Задача 7
```py
a = input().strip()
alf = 'QWERTYUIOPASDFGHJKLZXCVBNM'
ch = '0123456789'
bukv = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
start = 0
for i in range(len(a)):
    st = a[i]
    if st in alf:
        start = i
        break
second = 0
for i in range(len(a)):
    st = a[i]
    if st in ch and a[i + 1] in bukv:
        second = i + 1
        break
step = second - start
ans = []
i = start
while i < len(a):
    ans.append(a[i])
    if a[i] == '.':
        break
    i += step
print(''.join(ans))
```
![Задание со звёздочкой](/images/lab1/img_7.png)

# Лабораторная работа №2
Задача 1
```py
def min_max(nums):
    if len(nums) == 0:
        raise ValueError
    minimumchik = min(nums)
    maxichek = max(nums)
    return (minimumchik, maxichek)
```
![Первая](/images/lab2/ex1.png)

Задача 2
```py
def unique_sorted(nums):
    otvetik = sorted(set(nums))
    return otvetik
```
![Первая](/images/lab2/ex2.png)

Задача 3
```py
def flatten(nums):
    otvetik = []
    for e in nums:
        if type(e) == list or type(e) == tuple:
            for i in range(len(e)):
                if e[i] != '':
                    otvetik.append(e[i])
        else:
            raise TypeError
    return otvetik
```
![Первая](/images/lab2/ex3.png)

Задача 4
```py
def transpose(mat):
    new_mat = []
    if len(mat) == 0:
        return []
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    for stolbik in range(kol_simv):
        new_strochechka = []
        for strochechka in range(len(mat)):
            new_strochechka.append(mat[strochechka][stolbik])
        new_mat.append(new_strochechka)
    return new_mat
```
![Первая](/images/lab2/ex4.png)

Задача 5
```py
def row_sums(mat):
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    otvetik = []
    for elem in mat:
        otvetik.append(sum(elem))
    return otvetik
```
![Первая](/images/lab2/ex5.png)

Задача 6
```py
def col_sums(mat):
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    otvetik = [0] * len(mat[0])
    for strochechka in mat:
        for stolbik in range(len(strochechka)):
            otvetik[stolbik] = otvetik[stolbik] + strochechka[stolbik]
    return otvetik
```
![Первая](/images/lab2/ex6.png)

Задача 7
```py
def format_record(tuptup):
    otvetik = ''
    if type(tuptup) != tuple:
        raise TypeError
    if len(tuptup) == 3:
        fio = tuptup[0]
        gruppochka = tuptup[1]
        gpa = tuptup[2]
        if type(fio) == str and type(gruppochka) == str and type(gpa) == float and len(fio.split()) >= 2:
            fio = fio.split()
            if len(fio) == 2:
                fam = fio[0].capitalize()
                name = fio[1].capitalize()
                new_fio = f'{fam} {name[0]}.,'
            if len(fio) == 3:
                fam = fio[0].capitalize()
                name = fio[1].capitalize()
                otch = fio[2].capitalize()
                new_fio = f'{fam} {name[0]}.{otch[0]}.,'
            new_gruppochka = f'гр. {gruppochka},'
            otvetik = f'{new_fio} {new_gruppochka} {gpa:.2f}'
            return otvetik
        else:
            raise ValueError
    else:
        raise ValueError

```
![Первая](/images/lab2/ex7.png)

# Лабораторная работа №3
Задача A
```py
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


print("\n")
print("Тесты count_freq и top_n")


def top_n(freq, n = 2):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

tests = [["a", "b", "a", "c", "b", "a"], ["bb", "aa", "bb", "aa", "cc"]]

for array in tests:
    result = top_n(count_freq((array)))
    print(f"{array} - {result}")
```
![A](/images/lab3/exA1.png)
![A](/images/lab3/exA2.png)
![A](/images/lab3/exA3.png)

Задача B
```py
import sys
import re

sys.path.append('D:\python_labs\src')

def normalize(text, *, casefold = True, yo2e = True):
    text = re.sub(r"[\t\r\n\f\v]", " ", text)
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = re.sub(r" +", " ", text)
    return text.strip()

def tokenize(text):
    clear_text = re.sub(r'[^\w\s-]', ' ', text)
    new_text = clear_text.split()
    return new_text

def count_freq(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

def top_n(freq, n = 2):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


a = sys.stdin.read().strip()
norm = normalize(a)
token = tokenize(norm)
print("Всего слов:", len(token))
count = count_freq(token)
print("Уникальных слов:", len(count))
top = top_n(count)
print("Топ-5:")

for element in top:
    print(str(element[0]) + ":" + str(element[1]))
```
![B](/images/lab3/exB.png)


# Лабораторная работа №4

Задание А
```py
from pathlib import Path
import csv
# import sys
# sys.path.append(r'C:\Users\ameze\Desktop\python_labs\src')
def read_text(path, encoding ='utf-8'):
    path = Path(path)
    with open(path, 'r', encoding=encoding) as f:
        return f.read()

try:
    text = read_text(r'C:\Users\ameze\Desktop\python_labs\src\data\lab4\input.txt', encoding='utf-8')
    print(text)
except FileNotFoundError:
    print('Файл не найден')
except UnicodeDecodeError:
    print('Неподходящая кодировка')


def write_csv(rows, path, header):
    path = Path(path)
    if rows:
        last_dlina = len(rows[-1])
        for row in rows:
            if len(row) != last_dlina:
                raise ValueError
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv_maker = csv.writer(f, delimiter=',')
        if header:
            csv_maker.writerow(header)
        for row in rows:
            csv_maker.writerow(row)

write_csv([("word","count"),("test",3)], r'C:\Users\ameze\Desktop\python_labs\src\data\lab4\check.csv', None)
```
![A](images/lab4/lab4_exA1.png)
![A](images/lab4/lab4_exA2.png)

Задание В
```py
from pathlib import Path
import csv
import sys
sys.path.append(r'C:\Users\ameze\Desktop\python_labs\src')



from lib.normalize import normalize
from lib.tokenize import tokenize
from lib.count_freq_top_n_function import count_freq, top_n


def read_text(path, encoding='utf-8'):
    path = Path(path)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def report_writer(path, count_f, encoding='utf-8'):
    path = Path(path)
    sortirovka = top_n(count_f, len(count_f))
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv_maker = csv.writer(f, delimiter=',')
        csv_maker.writerow(('word', 'count'))
        for word, freq in sortirovka:
            csv_maker.writerow((word, freq))

try:
    text_i = read_text(r'C:\Users\ameze\Desktop\python_labs\src\data\lab4\input.txt', encoding='utf-8')
    norm = normalize(text_i)
    token = tokenize(norm)
    count_f = count_freq(token)
    top = top_n(count_f, 5)

    report_writer(r'C:\Users\ameze\Desktop\python_labs\src\data\lab4\report.csv', count_f, encoding='utf-8')
    print('Всего слов:', len(token))
    print('Уникальных слов:', len(count_f))
    for t in top:
        print(t[0], ':', t[1])
except FileNotFoundError:
    print('Файл не найден')
except UnicodeDecodeError:
    print('Неподходящая кодировка')
```
![B](images/lab4/lab4_exB1.png)
![B](images/lab4/lab4_exB2.png)