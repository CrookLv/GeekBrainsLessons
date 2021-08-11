from sys import argv

name, hours_production, rate_per_hour, bonus = argv

print("Имя скрипта: ", name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", hours_production)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Зарплата сотрудника: ", (float(hours_production) * float(rate_per_hour)) + float(bonus))
