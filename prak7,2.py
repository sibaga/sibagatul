'''
УВВ-111
Создайте функцию make_desk, результатом работы которой является стол.
Стол определяется тремя параметрами: a и b - размерами столешницы в сантиметрах, а также названием.
'''


def make_desk(name, a, b):
    desk = [name, a, b]
    return desk


print(make_desk('IKEA small', 20, 20))
print(make_desk('IKEA medium', 90, 90))
print(make_desk('IKEA extra large', 700, 1200))