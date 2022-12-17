mas = []
while True:
    num = int(input('Введите элемент массива: '))
    if num == 55555:
        break
    mas.append(num)

sum_ch = 0
pr = 1
count_s = 0
count_p = 0

for i in range(len(mas)):
    if i % 2 == 0:
        count_p += 1
        pr *= mas[i]
    elif i % 2 != 0:
        count_s += 1
        sum_ch += mas[i]
if count_p == 0:
    pr = 0

print(f'сомножители = {count_p},произведение = {pr}')
print(f'слагаемые = {count_s},сумма = {sum_ch}')

