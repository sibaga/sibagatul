'''
Напишите программу, которая считывает число и проверяет входит ли
число в промежутки: [-300;300] или [1000;1600]. Если число не входит
промежутки, пользователь вводит повторно, до тех пор, пока число не
будет частью промежутков.
Программа выводит число «The number is: », если число входит в
промежуток и выводит «Invalid number!», если не входит.

'''
num = int(input('Введите число:'))
while not (-300 <= num <= 300 or 1000 <= num <= 1600):
    print('Invalid number!')
    num = int(input('Введите число:'))
print('The number is:', num)