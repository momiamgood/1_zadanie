B = int(input('Введите В: '))
sum_b = 0

while True:
    num = int(input('Введите числа: '))
    if num % B == 0:
        sum_b += num
    elif num < 0:
        break
print(sum_b)
