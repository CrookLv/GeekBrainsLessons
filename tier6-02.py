# author - Vyacheslav Gusev

goods = []
while input("Хотели бы вы добавить товар? Введите +/-: ") == '+':
    number = int(input("Введите кол-во продукта: "))
    features = {}
    while input("Хотели бы вы добавить параметры продукта? Введите +/-: ") == '+':
        feature_key = input("Введите характеристику продукта: ")
        feature_value = input("Введите значение характеристики: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)

# Пока самое сложное задание, хотелось бы объяснений его выполнения, я с трудом его выполнил, так как у меня всё плохо с математическим мышлением. 
