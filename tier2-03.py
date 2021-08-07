''' author - Vyacheslav Gusev '''

def my_f(name, secname, birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {secname} Год рождения: {birth}'
                 f'Город: {city} Email: {email} Номер телефона: {phone}')

my_f(
    name=input('Имя: '),
    secname=input('Фамилия: '),
    birth=input('Год Рождения: '),
    city=input('Город: '),
    email=input('email: '),
    phone=input('Номер телефона: '),
)
