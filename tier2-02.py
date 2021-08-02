# author - Vyacheslav Gusev

my_list = []
while len(my_list) < 5:
  add = input(str('Введите элемент: '))
  my_list.append(add)
if len(my_list) % 2 == 0:
  i = 0
    while i < len(my_list):
      el = my_list[i]
      my_list[i] = my_list[i+1]
      my_list[i+1] = el
      i += 2
else:
  i = 0
    while i < len(my_list) - 1:
      el = my_list[i]
      my_list[i] = my_list[i+1]
      my_list[i+1] = el
      i += 2
print(my_list)
