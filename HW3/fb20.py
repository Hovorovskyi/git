#import sys
#filename = sys.argv[1]

f = open('fizzbuzz20.txt', 'r')

for line in f:
    l = line.split()
    fizz = int(l[0])
    buzz = int(l[1])
    number = int(l[2])
    for res in range(1, number + 1):
        if res % fizz != 0 and res % buzz != 0:
            print(res)
        elif res % fizz == 0 and res % buzz != 0:
            print('F')
        elif res % buzz == 0 and res % fizz != 0:
            print('B')
        else:
            print('FB')
    print('\n')

f.close()