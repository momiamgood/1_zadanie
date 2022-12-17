a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = int(input('Введите d: '))

if a * b < c * d:
    print('Прямоугольник AB поместится в CD')
    if (a < c or a < b) and (b < c or b < d):
        print('Прямоугольник поместится параллельно')
else:
    print('Прямоугольник не поместится в другой')
