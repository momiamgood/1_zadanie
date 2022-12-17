mas = []
N = int(input('Введите количество элементов: '))

count_3 = 0
count_p = 0
sum_p = 0

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)
    if num % 3 == 0:
        count_3 += 1
    elif num % 2 == 0:
        count_p += 1
        sum_p += num
sr_a = sum_p / count_p

mas.insert(0, count_3)
mas.insert(N+1, sr_a)
print(mas)
