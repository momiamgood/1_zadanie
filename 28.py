sum_c = 0

while True:
    num = int(input('Введите числа: '))
    if num != 0 and num != 99999:
        sum_c += num
    elif num == 0:
        print(sum_c)
    if num == 99999:
        break
print(sum_c)
