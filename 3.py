l = []
am = int(input('Введите количество строк'))
for i in range(am):
    a = str(input('Введите строку')).replace('?', '*')
    l.append(a)
print(l)
