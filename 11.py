N = int(input('Введите количество элементов массива: '))
mas = []

mas_o = []
mas_p = []

for i in range(N):
    num = int(input('Введите элемент массива: '))
    mas.append(num)

for r in range(N):
    if mas[r] < 0:
        mas_o.append(mas[r])
    elif mas[r] > 0:
        mas_p.append(mas[r])

print(mas)
print(mas_o)
print(mas_p)
