s = 0
count = 0
while True:
    count += 1
    l = int(input('Введите положительное число'))
    if l > 0:
        if l % 2 == 0:
            s += (l ** 2)
            print(s)
        elif l % 2 != 0:
            s += -l
            print(s)
    elif l < 0:
        count=-1
        break

print(s)
print(count)
