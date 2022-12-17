mas = []
N = int(input('Введите количество элементов: '))

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)

for i in range(N-1):
    if mas[i] == 0:
        mas.pop(mas[i-1])

print(mas)
