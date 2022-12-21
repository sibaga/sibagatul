# 5.1
# Сгенерируйте массив случайных чисел любой длины и интервала и выведите его
# Пример:
# [5, 55, 337, 490, 10, 540]
import random

i = []
for a in range(random.randint(1, 100)):
    i.append(random.randint(1, 100))
print(i)