mas = []
N = int(input('Введите N: '))
for i in range(N):
    num = int(input('Введите эл массива: '))
    mas.append(num)

count_nulls = 0

for i in range(N - 1):
    if mas[i] == 0 and mas[i + 1] == 0:
        count_nulls += 1

if count_nulls>0:
    print('В массиве есть два идущих подряд нуля')
else:
    print('В массиве нет идущих подряд нулей')
