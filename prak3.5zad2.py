# 3.5.2
# Казино
# У игрока имеется 100 у.е.
# Он вводит ставку и цвет (красное/чёрное)
# Производится рандом рулетки и игрок либо теряет свою ставку,
# либо получает 180% ставки на счёт.
# Игра заканчивается, если у игрока не осталось денег, либо по вводу STOP
# Ставка не должна превышать баланс
import random

continuee = ''
money = 100
color = ''
while continuee != 'нет' and money != 0 and continuee != 'stop' and color != 'stop':
    bet = input('сколько вы хотите поставить:')
    if bet == 'stop': break
    money -= int(bet)
    color = input('на что вы хотите поставить?(красное, черное, зеленое)')
    if color == 'stop': break
    y = random.randint(0, 37)
    if color == 'красное' and 1 <= y <= 18:
        money += int(bet) * 18 / 10
        print('вы выиграли:', int(bet) * 18 / 10, '\nваш баланс:', money)
    if color == 'черное' and 19 <= y <= 36:
        money += int(bet) * 18 / 10
        print('вы выиграли:', int(bet) * 18 / 10, '\nваш баланс:', money)
    if color == 'зеленое' and (y == 0 or y == 37):
        money += int(bet) * 18
        print('вы выиграли:', int(bet) * 18, '\nваш баланс:', money)
print('ваш баланс:', money)
