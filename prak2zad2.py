# сибагатулин артем увв 111
# практика 2 задание 2
"""
Напишите программу, которая считывает из консоли фрукт (banana / apple
/ orange / grapefruit / kiwi / pineapple / grapes), день недели (Monday /
Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday), количество
кг (вещественное число), и рассчитывает стоимость в соответствии с
ценами в таблицах выше. Выведите результат, округленный до 2 цифр
после точки. Если пользователь ввел неправильный день недели или
неправильное название фрукта, выведите «error».

"""

price = 0
fruit = input('что хотите купить?(banana apple orange grapefruit kiwi pineapple grapes)\n')
day = input('когда?(Monday Tuesday Wednesday Thursday Friday Saturday Sunday)\n')
wight = float(input('сколько?\n'))
if (
        fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes') and (
        day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday'):
    if day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            price = wight * 2.70
        elif fruit == 'apple':
            price = wight * 1.25
        elif fruit == 'orange':
            price = wight * 0.90
        elif fruit == 'grapefruit':
            price = wight * 1.60
        elif fruit == 'kiwi':
            price = wight * 3.00
        elif fruit == 'pineapple':
            price = wight * 5.60
        elif fruit == 'grapes':
            price = wight * 4.20
    else:
        if fruit == 'banana':
            price = wight * 2.50
        elif fruit == 'apple':
            price = wight * 1.20
        elif fruit == 'orange':
            price = wight * 0.85
        elif fruit == 'grapefruit':
            price = wight * 1.45
        elif fruit == 'kiwi':
            price = wight * 2.70
        elif fruit == 'pineapple':
            price = wight * 5.50
        elif fruit == 'grapes':
            price = wight * 3.85
    print('цена: ', price)
else:
    print('error')
