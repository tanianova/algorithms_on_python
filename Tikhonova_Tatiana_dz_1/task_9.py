# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))

if b < a < c or b > a > c:
    print('первое число - среднее')
elif a < b < c or a > b > c:
    print('второе число - среднее')
else:
    print('третье число - среднее')
