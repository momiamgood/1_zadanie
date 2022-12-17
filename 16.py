import math

a = int(input('Введите а: '))
h = int(input('Введите h: '))
r = int(input('Введите r: '))

M = int(input('Введите объем М жидкости: '))

v_cub = a ** 3
v_cil = math.pi * (r ** 2) * h

if M <= v_cil and M <= v_cub:
    print('Жидкость поместится и в куб и в цилиндр')
elif M <= v_cil:
    print('Жидкость поместится в цилиндр')
elif M <= v_cub:
    print('Жидкость поместится куб')
