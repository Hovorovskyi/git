import sys
from collections import Counter
filename = sys.argv[1]

f = open(filename, 'r')

def res(f):
    f = f.split()
    c = Counter(f)
    return c

print(list(map(res, f)))

f.close()