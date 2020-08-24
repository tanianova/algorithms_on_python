# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

num_1 = deque('A2')
num_2 = deque('C4F')
summa = deque()
remain = 0

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(num_1) < len(num_2):
    num_1, num_2 = num_2, num_1
while len(num_2) != len(num_1):
    num_2.appendleft('0')


for i in range(len(num_1)):
    spam_num_1 = list_of_numbers.index(num_1.pop())
    spam_num_2 = list_of_numbers.index(num_2.pop())
    spam_sum = spam_num_1 + spam_num_2 + remain
    if spam_sum <= 15:
        summa.append(list_of_numbers[spam_sum])
        remain = 0
    else:
        summa.append(list_of_numbers[spam_sum - 16])
        remain = 1
summa.reverse()
print(summa)
