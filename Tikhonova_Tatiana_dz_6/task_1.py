# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# указать версию и разрядность вашей ОС и интерпретатора Python;
#  написать общий вывод: какой из трёх вариантов лучше и почему.
import random
import sys


def total(x):
    memory = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items:
                memory += total(key) + total(value)
        elif not isinstance(x, str):
            for item in x:
                memory += total(item)
    return memory


# 4. Определить, какое число в массиве встречается чаще всего.
MIN_ITEM = 1
MAX_ITEM = 100
n = 10
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
print(a)

# вариант 1
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
    print(f'число {num} встречается {most_common} раз')
else:
    print('все числа уникальны')


print(f'1 вариант: '
      f'{total(a) + total(num) + total(most_common) + total(i) + total(frequency) + total(k)} '
      f'байта')

# 2 вариант
counter = {}
frequency = 1
num = None
for number in a:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
    if counter[number] > frequency:
        frequency = counter[number]
        num = number
if num is not None:
    print(f'Число {num} встречается {frequency} раз(а)')
else:
    print('Все элементы уникальны')

print(f'2 вариант: '
      f'{total(a) + sys.getsizeof(counter) + total(frequency) + total(num) + total(number)} '
      f'байта')

# 3 вариант
a_set = set(a)
num = None
most_common = 1
for number in a_set:
    frequency = a.count(number)
    if frequency > most_common:
        most_common = frequency
        num = number
print(f'Число {num} встречается {most_common} раз(а)' if most_common > 1 else 'Все элементы уникальны')

print(f'3 вариант: '
      f'{total(a) + total(a_set) + total(most_common) + total(num) + total(number) + total(frequency)}'
      f' байта')


# ОС windows 10 версия 1803
# в свойствах компьютера пишет 64-разрядная операционная система, но когда я проверила простое целое число на
# размерность, он выдал 14.
# python 3.8
# вывод: первый вариант занимает меньше всего памяти, так как в нем нет словаря и множества.
# а еще, есть вероятность, что у второго варианта решения была неправильно посчитана выделенная память, потому что
# объект counter хоть и является словарем, но выдавал мне ошибку, что он не итерируется. долго думала, но так и
# не додумала, в чем проблема, поэтому посчитала его через sys.getsizeof ((