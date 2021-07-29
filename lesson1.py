# Tier 1
number = int(input('Введите число: '))
string = input(str('Введите слово: '))
a = number
b = string
print(a)
print(b)

# Tier 2 
a=int(input('Введите секунды: '))
h=str(a//3600)
m=(a//60)%60
s=a%60
if m<10:
    m='0'+str(m)
else:
    m=str(m)
if s<10:
    s='0'+str(s)
else:
    s=str(s)
print(h+':'+m+':'+s)

# Tier 3
n = int(input("Введите число n: "))
numb = str(n)
n1 = numb + numb
n2 = numb + numb + numb
summ = n + int(n1) + int(n2)
print("Результат равен:", summ)

# Tier 4
a = int(input())
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

# Tier 5
a = int(input('Введите выручку вашей фирмы: '))
b = int(input('Введите издержку вашей фирмы: '))
if a > b:
	prof = a - b
	rent = a / b
	print(f'Поздравляем, вы имеете {prof} профита.')
	worker = int(input('Кол-во рабочих: '))
	print(f'{prof/worker} для одного рабочего.')
elif a == b:
	print('Ваша фирма в неплохом состоянии.')
else:
	print('Ваша фирма в убытке!')

# Tier 6
a = float(input("Введите старт: "))
b = float(input("Введите финиш: "))
day = 1
if a > b:
	print(day)
while a < b:
	a = a + a/10
	day += 1
print(day)

# Tier 7
