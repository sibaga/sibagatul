#сибагатулин артем увв 111
#практика 2 задание 4
'''Градусы – целое число в интервале [10...42]
Строка – время суток - "Morning", "Afternoon", "Evening".
Программа выводит фразу: "It's {градусов} degrees, get your {одежда} and
{обувь}."
Примеры ввода и вывода:
'''
temp = float(input('введите температуру:'))
timeofday = input('время суток(Morning, Afternoon, Evening):')
odejda = ['Sweatshirt', 'Shirt', 'T-Shirt', 'Swim Suit']
obuv = ['Sneakers', 'Moccasins', 'Sandals', 'Barefoot']
if 10 <= temp <= 18:
    if timeofday == 'Morning':
        print("It's ", temp, " degrees, get your", odejda[0], "and", obuv[0])
    elif timeofday == 'Afternoon':
        print("It's ", temp, " degrees, get your", odejda[1], "and", obuv[1])
    elif timeofday == 'Evening':
        print("It's ", temp, " degrees, get your", odejda[1], "and", obuv[1])
if 18 <= temp <= 24:
    if timeofday == 'Morning':
        print("It's ", temp, " degrees, get your", odejda[1], "and", obuv[1])
    elif timeofday == 'Afternoon':
        print("It's ", temp, " degrees, get your", odejda[2], "and", obuv[2])
    elif timeofday == 'Evening':
        print("It's ", temp, " degrees, get your", odejda[1], "and", obuv[1])
if temp >= 25:
    if timeofday == 'Morning':
        print("It's ", temp, " degrees, get your", odejda[2], "and", obuv[2])
    elif timeofday == 'Afternoon':
        print("It's ", temp, " degrees, get your", odejda[3], "and", obuv[3])
    elif timeofday == 'Evening':
        print("It's ", temp, " degrees, get your", odejda[1], "and", obuv[1])
