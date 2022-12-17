P = int(input('Введите P: '))
H = int(input('Введите H: '))

sum_p = 0
pr_h = 1
count_p = 0
count_h = 0

while True:
    num = int(input('Введите числа: '))
    if num < P:
        sum_p += num
        count_p += 1
        if num < H:
            pr_h *= num
            count_h += 1
    else:
        break

if count_h == 0:
    pr_h = 0

print(f'сумма чисел меньше Р = {sum_p}, количество = {count_p}')
print(f'произведение чисел меньше H = {pr_h}, количество = {count_h}')
