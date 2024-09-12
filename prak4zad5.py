'''
'''
num = input('введите число:')
suma = 0
primesum = 0
while num != 'stop':
    if int(num) >= 0:
        suma += int(num)
        if int(num) == 1:
            primesum += 1
        else:
            if int(num) == 2:
                primesum += 2
            for i in range(2, int(num) // 2):
                if int(num) % i == 0:
                    break
                else:
                    primesum += int(num)
    else:
        print(num, ' is negative.')
    num = input('введите число:')
print('Sum of all prime numbers is:', primesum)
print('Sum of all non prime numbers is:', suma)
