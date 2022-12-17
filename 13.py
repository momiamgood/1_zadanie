N = int(input('Введите количество элементов массива: '))
mas = []

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)

for i in range(0, N-1, 2):
    mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
