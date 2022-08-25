n = 5
a = 0
b = ''
for i in range(1, n+1):
    a += 1
    b = b + str(i)
    if a != 0:
        print(b)
    a -= 1
