# oksimiron = input("введите первую последовательность:")
# oksimiron = oksimiron.split(" ")
# dart_veider = input("введите вторую последовательность:")
# dart_veider = dart_veider.split(" ")
# result=list(set(oksimiron) & set(dart_veider))
# print(result)


a = input('Введите текст: ').split(" ")
b = input('Введите текст: ')
for i in a:
	if i in b:
		print(i)