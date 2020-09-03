# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
a[max_index], a[min_index] = a[min_index], a[max_index]
print(a)

