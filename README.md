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