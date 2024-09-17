'''
УВВ-111
Создайте функцию покупки игры в каком-нибудь магазине (Steam, PS Store, Epic Games). Пусть она называется buy_game.
Функция должна принимать сумму денег на вашем счету, название игры и её цену. Функция должна вывести покупку в консоль, как показано в примере.
Если денег на счету не хватило, необходимо вывести ошибку, как показано в примере.
Результатом работы функции должен быть остаток денег на вашем счету в результате покупки.
'''

balance = 20000


def buy_game(balance, game, cost):
    if balance - cost >= 0:
        print(f'Покупаем "{game}" за {cost} р')
        balance -= cost
    else:
        print(f'Не удалось купить "{game}" за {cost} р.')

    return balance


balance = buy_game(balance, 'God Of War: Ragnarok', 5499)
balance = buy_game(balance, 'Call Of Duty', 4899)
balance = buy_game(balance, 'The Witcher 3', 8499)
balance = buy_game(balance, 'pvz garden warfare', 100000)

print(f'На счету осталось: {balance} р')
