d = {
    'Ivanov': (5, 4, 5),
    'Shevchenko': (5, 5, 5),
    'Kosov': (4, 3, 4)
}

def m(a):
    a = []
    for key in d:
        a += key
    return key

print (list(map(m, d)))