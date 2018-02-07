i = int(input("Введите число:"))
z = 0
while i > 0:
	z = z + i % 10
	i = i // 10
print(z)