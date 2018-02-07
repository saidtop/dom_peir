fib_1 = 1
fib_2 = 1
a = int(input("Число Фибоначчи:"))
i = 2 
while i < a:
    fib_sum = fib_2 + fib_1
    fib_1 = fib_2
    fib_2 = fib_sum
    i += 1
print (fib_sum)