import random

N = int(input('Введите количество элементов массива: '))
mas = []
count_o = 0
count_p = 0

for i in range(N):
    num = int(input('Введите элемент массива: '))
    if num < 0:
        count_o += 1
    elif num > 0:
        count_p += 1
    mas.append(num)

if count_o > count_p:
    for w in range(count_o - count_p):
        num = random.randint(1, 100)
        mas.append(num)
elif count_o < count_p:
    for w in range(count_p - count_o):
        num = random.randint(1, 100)
        mas.append(num)

print(mas)
