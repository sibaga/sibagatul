'''уВВ-111 6.1
сибагатулин
 Создать коллекцию супергероев (каждый супергерой - объект с параметрами)
 Найти и вывести супергероя с наибольшим количеством подвигов
'''
Leonardo = {
    'Name': 'Leonardo',
    'Weapon': 'catana',
    'heroic_deeds': 456
}
Donatello = {
    'Name': 'Donatello',
    'Weapon': 'Bo',
    'heroic_deeds': 345
}
Raphael = {
    'Name': 'Raphael',
    'Weapon': 'Sai',
    'heroic_deeds': 543
}

Michelangelo = {
    'Name': 'Michelangelo',
    'Weapon': 'Nunchaku',
    'heroic_deeds': 394
}

Teenage_Mutant_Ninja_Turtles = [Leonardo, Donatello, Raphael, Michelangelo]

maxi = a = max_heroic_deeds = 0

for hero in Teenage_Mutant_Ninja_Turtles:
    if maxi < hero['heroic_deeds']:
        maxi = hero['heroic_deeds']
        max_heroic_deeds = a
    a += 1

print(Teenage_Mutant_Ninja_Turtles[max_heroic_deeds])
pass
