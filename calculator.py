def addition(a,b):
	print(a+b)
def subtraction(a,b):
	print(a-b)
def multiplication(a,b):
	print(a*b)
def division(a,b):
	print(a/b)
def  power(a,b):
	print(a**b)
def remainderofthedivision(a,b):
	print(a % b)
def integerpartfromdivision(a,b):
	print(a//b)
while True:
	a = int(input("""Какую операцию вы хотите совершить?
		1.Сложение
		2.Вычитание
		3.Умножение
		4.Деление
		5.Возведение в степень(первое число-второе степень)
		6.Остаток от деления
		7.Целая часть от деления
		:"""))
	if a==1:
		addition(int(input("введите первое число:")),int(input("введите второе число:")) )
	elif a==2:
		subtraction(int(input("введите первое число:")),int(input("введите второе число:")))
	elif a==3:
		multiplication(int(input("введите первое число:")),int(input("введите второе число:")))
	elif a==4:
		division(int(input("введите первое число:")),int(input("введите второе число:")))
	elif a==5:
		power(int(input("введите первое число:")),int(input("введите второе число:")))
	elif a==6:
		remainderofthedivision(int(input("введите первое число:")),int(input("введите второе число:")))
	elif a==7:
		integerpartfromdivision(int(input("введите первое число:")),int(input("введите второе число:")))
	else:
		print("Тут нет такой операций")
		break


