''' author - Vyacheslav Gusev '''

def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result


print(f'Dозведение в степень (1 Вариант): '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')


print(f'Dозведение в степень (2 Вариант): '
      f'{my_func_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')
