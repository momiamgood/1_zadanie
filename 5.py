M = int(input('Введите количество строк'))
for b in range(M):
    a = str(input('Введите строку'))
    count = 0
    for i in a:
        if i == 'а' or i == 'е' or i == 'о' or i == 'ы' or i == 'у' or i == 'я' or i == 'э' or i == 'ю' or i == 'и':
            count += 1
    print(a, count)
