a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

m = int(input('Введите m: '))
k = int(input('Введите k: '))


if a*c < m*k or a*b < m*k or b*c < m*k:
    print('Коробка пройдет в дверь')
else:
    print('Коробка в дверь не пройдет')
