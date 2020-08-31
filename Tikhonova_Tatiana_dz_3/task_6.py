# 6.  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(a)


max_index = 0
min_index = 0

for i in range(len(a)):
    if a[i] > a[max_index]:
        max_index = i
    if a[i] < a[min_index]:
        min_index = i


summa = 0
if min_index < max_index:
    for i in range(min_index + 1, max_index):
        summa += a[i]
elif min_index > max_index:
    for i in range(max_index + 1, min_index):
        summa += a[i]

print(summa)


