
summer = int(input('Please, enter amount ', ))

banknotes = [500, 100, 50, 10]

if summer % 10 != 0:
    print('We can\'t give you this sum, please enter sum equivalent to 10')
else:
    for x in banknotes[::-1]:
        num = summer // x
        summer -= num * x
        print(num, x)
