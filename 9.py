import math

A = int(input('Введите длинну массива'))
mas = []
sum_o = 0
sum_p = 0

for a in range(A):
    num = int(input('Введите элемент массива'))
    mas.append(num)

for i in range(A):
    print(mas[i])
    if mas[i] < 0:
        sum_o += math.fabs(mas[i])
    elif mas[i] > 0:
        sum_p += math.fabs(mas[i])

print(sum_p)
print(sum_o)

if sum_p > sum_o:
    mas.append(sum_p - sum_o)
elif sum_o > sum_p:
    mas.append(sum_o - sum_p)

print(mas)
