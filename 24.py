mas = []
N = int(input('Введите количество элементов: '))

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)

for i in range(N):
    if mas[i] == 0:
        mas[i] = mas[i - 1] + mas[i - 2]

print(mas)
