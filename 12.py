N = int(input('Введите количество элементов массива: '))
mas = []

count = 0
sum_p = 0

for i in range(N):
    num = int(input('Введите элемент массива: '))
    count += 1
    if num > 0:
        sum_p += num
    else:
        pass
    mas.append(num)

mas.insert(0, sum_p)
mas.insert(1, count)
print(mas)
