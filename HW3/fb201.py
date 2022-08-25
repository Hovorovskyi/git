import sys
filename = sys.argv[1]

f = open(filename, 'r')
t = open('F:\Projects PyCharm\Python\ 2.0\HW3\mfizzbuzz201.txt', 'w')
for line in f:
    l = line.split()
    fizz = int(l[0])
    buzz = int(l[1])
    number = int(l[2])
    for res in range(1, number + 1):
        if res % fizz != 0 and res % buzz != 0:
            t.write(res)
            print(res)
        elif res % fizz == 0 and res % buzz != 0:
            t.write('F')
            print('F')
        elif res % buzz == 0 and res % fizz != 0:
            t.write('B')
            print('B')
        else:
            t.write('FB')
            print('FB')
    t.write('\n')
    print('\n')
t.close()
f.close()