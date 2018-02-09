a = int(input("n="))
b = []
for i in range(2, a+1):
    for k in range(2, i):
        if i % k == 0:
        
            break
    else:
        b.append(i)
print (b)