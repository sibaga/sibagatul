#сибагатулин артем увв 111
#практика 2 задание 5
'''Ваши друзья очень любят ходить на рыбалку, и они так увлечены ею, что
решили отправиться на рыбалку на лодке. Стоимость аренды лодки
зависит от сезона и количества рыбаков.
Цена зависит от сезона:
• Стоимость аренды судна весной составляет 3000 рублей.
• Стоимость аренды судна летом и осенью составляет 4200 рублей
• Стоимость аренды судна в зимний период составляет 2600 рублей
В зависимости от количества, группы пользуются скидкой:
• Если группа до 6 человек включительно - скидка 10%.
• Если группа от 7 до 11 человек включительно - скидка 15%.
• Если группа от 12 и выше - скидка 25%.
Рыбакам доступна дополнительная 5% скидка, если их количество четное,
но если осень - у них нет дополнительной скидки.

В программу водится 3 значения:
• Бюджет группы - целое число в диапазоне [1 ... 8000]
• Сезон – строка: "Spring", "Summer", "Autumn", "Winter"
• Количество рыбаков - целое число в диапазоне [4...18]
Вывод:
Выводится строка:
• Если бюджета хватает, "Yes! You have {оставшиеся деньги} rubles
left."
• Если бюджета недостаточно: "Not enough money! You need {сумма,
которой не хватает} rubles."
Суммы должны быть отформатированы с точностью до двух знаков после
запятой.
Примеры ввода и вывода:
'''

money = int(input('сколько у вас денег?'))
Season = input('время года(Spring, Summer, Autumn, Winter?)')
quantity = int(input('сколько вас?'))
discount = 0.0
price = 0.0
if 4 <= quantity <= 18 and 1 <= money <= 8000:
    if Season == 'Spring':
        price = 3000
    elif Season == 'Summer':
        price = 4200
    elif Season == 'Autumn':
        price = 4200
    elif Season == 'Winter':
        price = 2600
    if quantity < 7:
        discount = 1/10
    elif 7 <= quantity <= 11:
        discount = 15/100
    elif quantity > 12:
        discount = 25/100
    if quantity % 2 == 0 and Season != 'Autumn':
        discount += 5/100
    ost=money-price*(1-discount)
    if ost >= 0:
        print('Yes! You have ', round(ost), ' rubles left.')
    else:
        print('Not enough money! You need ', round(abs(ost)), ' rubles.')


else:
    print('error')
