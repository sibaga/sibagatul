'''
Вы ландшафтный дизайнер, и вы выполняете крупный заказ! Подсчитайте
стоимость заказа, учитывая стоимость работ (1 кв.м. - 7.61$) и с учетом
финальной скидки 18%.
'''
import math
print('сколько кв метров?')
price = float(input()) * 7.61
discount = price * 0.18
final_price = price - discount
print(f"The final price is:", "%.2f" % final_price, " $.\n"
      f"The discount is: ", "%.2f" % discount, " $")
