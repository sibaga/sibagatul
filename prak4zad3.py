'''Программа получает 2*n чисел (где n – количество пар). Первое и второе
число образуют пару, третье и четвертое тоже и т.д. Каждая пара имеет
значение - сумму составляющих ее чисел. Напишите программу, которая
проверяет, имеют ли все пары одинаковое значение или печатает
максимальную разницу между двумя последовательными парами. Если все
пары имеют одинаковое значение, выведите «Yes, value = {Value}», где
{Value} – значение суммы. В противном случае распечатайте "No, maxdiff =
{Difference}", где {Difference} – значение максимальной разницы между
последовательными суммами'''
kolvopar = int(input('введите кол-во пар:'))
maxdif=0
for i in range(kolvopar):
    a = int(input('введите число:'))
    a += int(input('введите число:'))
    if i%2==0:
        b=a
    else:
        c=a
    if i!=0 and c-b!=0:
        maxdif=abs(c-b)
if maxdif==0:
    print('Yes, value=', a)
else:
    print('No, maxdiff=', maxdif)
