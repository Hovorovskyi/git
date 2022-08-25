dict = {
    'Python': {
        'Fedya':'Ivanov',
        'Petya':'Petrov',
        'Dima':'Sidorov'
    },
    'FrontEnd': {
        'Taras':'Shevchenko',
        'Petya':'Petrov',
        'Max':'Pain'
    },
    'FullStack': {
        'Rob':'Fizz',
        'Max':'Buzz',
        'Taras':'Shevchenko'
    },
    'Java': {
        'Dima':'Hovorovskyi',
        'Tolya':'Ivanov',
        'Zed':'Max'
    }
}


def not_front(x):
    for d, i in x.items():
        if i in d[1]:
            pass
    return i

print(list(map(not_front, dict)))