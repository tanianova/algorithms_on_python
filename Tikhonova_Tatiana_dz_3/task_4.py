# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(a)

num = None
most_common = 1
for i in range(len(a)):
    frequency = 1
    for k in range(i + 1, len(a)):
        if a[i] == a[k]:
            frequency += 1
    if frequency > most_common:
        most_common = frequency
        num = a[i]

if most_common > 1:
    print(f'чаще всего встречается число {num}')
else:
    print('все числа встречаются одинаковое колво раз')




