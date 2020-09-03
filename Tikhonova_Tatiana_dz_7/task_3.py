# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы.
import random


def gnome(a):
    i = 1
    while i < len(a):
        if a[i - 1] <= a[i]:
            i += 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            if i > 1:
                i -= 1
    return a


m = 10
array = [random.randint(0, 100) for _ in range(2*m+1)]
print(array)
print(gnome(array))
print(f'медиана массива: {array[len(array)//2]}')
