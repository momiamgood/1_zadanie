L = []
M = int(input('Введите количество строк: '))
s = ''

for i in range(M):
	a = (input('Введите строку: '))
	L.append(a)
	if len(L[i]) > len(s):
		s = L[i]
	print(s)
	
for i in range(M):
	if len(L[i]) < len(s):
		L[i] = (len(s)-len(L[i]))*'*' + L[i]
		print(L[i])
	
print(L)
