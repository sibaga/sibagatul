# 5.2
# Создать случайное поле для крестиков-ноликов и вывести его
# Пример:
# 0 X 0
# 0 0 X
# X 0 0
import random


def a():
    r = random.randint(0, 1)
    if r:
        return 'X'
    else:
        return 'O'


i = []
for b in range(3):
    i.append([a(), a(), a()])
for a in range(3):
    print(i[a])
