fizz = int(input('Enter Fizz: '))
buzz = int(input('Enter Buzz: '))
number = int(input('Enter the third number: '))

for res in range(1, number+1):
    if res % fizz != 0 and res % buzz != 0:
        print(res)
    elif res % fizz == 0 and res % buzz != 0:
        print('F')
    elif res % buzz == 0 and res % fizz != 0:
        print('B')
    else:
        print('FB')
