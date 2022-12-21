""" УВВ-111 Сибагатулин
 Создать каталог магазина (каждый товар - объект с параметрами)
 Пример: { title: Деревянный стол, price: 3500, category: мебель }
 Сделать минимум 10 элементов и в минимум 3 категориях
 Найти и вывести только элементы одной категории, которую введёт пользователь
"""
banana = {
    'title': 'банан',
    'price': '100',
    'category': 'фрукты'
}
apple = {
    'title': 'яблоко',
    'price': '90',
    'category': 'фрукты'
}
kiwi = {
    'title': 'киви',
    'price': '250',
    'category': 'фрукты'
}
shower_gel = {
    'title': 'гель для душа',
    'price': '300',
    'category': 'гигиена'
}
toothpaste = {
    'title': 'зубная паста',
    'price': '150',
    'category': 'гигиена'
}
toothbrush = {
    'title': 'зубная щётка',
    'price': '300',
    'category': 'гигиена'
}
coca_cola = {
    'title': 'кока_кола',
    'price': '150',
    'category': 'напитки'
}
fanta = {
    'title': 'фанта',
    'price': '125',
    'category': 'напитки'
}
sprite = {
    'title': 'спрайт',
    'price': '140',
    'category': 'напитки'
}
catalog = [banana, apple, kiwi, shower_gel, toothpaste, toothbrush, coca_cola, fanta, sprite]
inp = input()
flag = False

if __name__ == "__main__":
    for product in catalog:
        if inp == product['category']:
            print(product)
            flag = True
    if not flag:
        print('товаров данной категории не найдено')
    pass
