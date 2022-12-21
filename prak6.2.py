'''
 УВВ-111
 сибагатулин
 Создать инвентарь игрока (каждый элемент инвентаря - объект с параметрами)
 Пример1: { name: Яблоко, count: 131, type: Food }
 Пример2: { name: Древний щит, count: 500, type: Armor }
 Пример3: { name: Алмаз, count: 64, type: stone }
 Красиво вывести инвентарь в консоль (название, количество и тип)
 Найти элемент с наибольшим количеством и вывести его название'''

first_slot = {
    'name': 'dirt',
    'count': 64,
    'type': 'block'
}
second_slot = {
    'name': 'wooden pickaxe',
    'count': 1,
    'type': 'tool'
}
third_slot = {
    'name': 'gold nugget',
    'count': 63,
    'type': 'resources'
}
fourth_slot = {
    'name': 'obsidian',
    'count': 3,
    'type': 'block'
}
fifth_slot = {
    'name': 'Beacon',
    'count': 1,
    'type': 'block'
}

inventory = [first_slot, second_slot, third_slot, fourth_slot, fifth_slot]

maxi = a = max_ind = 0

for slot in inventory:
    print(f'Номер слота: {a}, предмет: {slot["name"]}, количество: {slot["count"]}, тип предмета: {slot["type"]}.')
    if maxi < slot['count']:
        maxi = slot['count']
        max_ind = a
    a += 1
print(inventory[max_ind]['name'])
pass
