''' author - Vyacheslav Gusev '''

def my_f(a, b):
    try:
        return print(a / b)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')
    
my_f(
    a = int(input('Введите первое число: ')),
    b = int(input('Введите второе число: '))
)
