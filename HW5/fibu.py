import sys
filename = sys.argv[1]

f = open(filename, 'r')
t = open('F:\Projects PyCharm\Python\ 2.0\HW3\mfizzbuzz201.txt', 'w')

def fb(f, b, n):
    for i in range(1, n + 1):
        if i % f != 0 and i % b != 0:
            return i
        elif i % f == 0 and i % b != 0:
            return 'F'
        elif i % b == 0 and i % f != 0:
            return 'B'
        else:
            return 'FB'

t.write(map(fb, f))

t.close()
f.close()