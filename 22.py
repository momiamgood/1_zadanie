mas = []
N = int(input('Введите количество элементов: '))

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)

M = int(input('Введите количество элементов, которые нужно удалить: '))
K = int(input('Введите индекс: '))

for i in range(M):
    mas.pop(K)

print(mas)
