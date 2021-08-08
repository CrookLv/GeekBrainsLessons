''' author - Vyacheslav Gusev '''

def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('аргумент 1')),
    int(input('аргумент 2')),
    int(input('аргумент 3')),
)
