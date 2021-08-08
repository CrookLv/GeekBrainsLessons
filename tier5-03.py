''' author - Vyacheslav Gusev '''

print(max([sum([int (numeric) for numeric in number]) for number in input('Введите цифровые значения в строку, используя пробел: ').split(' ')]))
