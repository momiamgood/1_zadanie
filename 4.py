M = int(input('Введите количество строк'))
count = 0
for b in range(M):
    a = str(input('Введите строку'))
    count = a.count(' ')
    print(a, count)
