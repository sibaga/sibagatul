#Сибагатулин Увв-111 пракитка 3 задание 3
'''Напишите программу, которая считывает n целых чисел (n > 0), введенных
пользователем, и находит самое меньшее из них. Сначала вводится число
чисел n, а затем сами числа, по одному в каждой строке.'''
c = int(input('введите кол-во числе:'))
small = 10000000000000
while c > 0:
    num = int(input('введите число:'))
    if num < small:
        small = num
    c -= 1
print(small)