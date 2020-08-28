# Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

import collections

n = int(input('колво предприятий: '))
sum_profit = 0
firms = collections.defaultdict(int)

for i in range(n):
    name = input(f'название {i+1} предприятия: ')
    for k in range(1, 5):
        profit = int(input(f'прибыль предприятия за {k} квартал: '))
        firms[name] += profit
        sum_profit += profit

average_profit = sum_profit / n

print(f'средняя прибыль всех предприятий за год - {average_profit}')

for i in firms:
    if firms[i] > average_profit:
        print(f'предприятия с прибылью выше средней: {i}')
    else:
        print(f'предприятия с прибылью ниже средней: {i}')




