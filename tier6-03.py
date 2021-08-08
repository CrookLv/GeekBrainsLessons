''' author - Vyacheslav Gusev '''

def int_func(text):
    return text.title()

output = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output.append(int_func(word))

print(f'Вывод: {" ".join(output)}')
