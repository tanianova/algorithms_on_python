# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(left_part, right_part):
    sorted_list = []
    left_index = 0
    right_index = 0

    for _ in range(len(left_part) + len(right_part)):
        if left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] <= right_part[right_index]:
                sorted_list.append(left_part[left_index])
                left_index += 1
            else:
                sorted_list.append(right_part[right_index])
                right_index += 1

        elif left_index == len(left_part):
            sorted_list.append(right_part[right_index])
            right_index += 1
        elif right_index == len(right_part):
            sorted_list.append(left_part[left_index])
            left_index += 1
    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)


a = [round(random.uniform(0, 49.99), 2) for _ in range(10)]
print(a)
print(merge_sort(a))
