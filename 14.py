year = int(input('Введите год: '))
if year % 4 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')

vek = year % 100 + 1
print('Век', vek)
