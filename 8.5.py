def a(a, b , c ,):
	D = b*b - 4*a*c
	if D < 0:
		print('Действительных корней нет')
		return
	elif D == 0:
		print('есть 2 одинаковых корня')
		X = -b/(2*a)
		return X
	else:
		print('2 различных корня')
		x1 = (-b + D**0.5)/(2*a)
		x2 = (-b - D**0.5)/(2*a)
		return x1, x2
y1, y2 = a(int(input("a:")),int(input("b:")),int(input("c:")))
print(y1, y2)