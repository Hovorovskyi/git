import sys
filename = sys.argv[0]

f = open(filename, 'r')
print(f.read()[::-1])
f.close()