
def is_prime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def check(x):
    if is_prime(x):
        return (x*x)
    else:
        return ('No')



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(check, a)))