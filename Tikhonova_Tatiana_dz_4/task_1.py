# 4. Определить, какое число в массиве встречается чаще всего.
import random
import timeit
import cProfile

MIN_ITEM = 1
MAX_ITEM = 100


# вариант 1
def func_1(n):
    a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
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
        return f'число {num} встречается {most_common} раз'
    else:
        return 'все числа уникальны'


print(timeit.timeit('func_1(10)', number=100, globals=globals()))  # 0.002423307999999999
print(timeit.timeit('func_1(20)', number=100, globals=globals()))  # 0.0054917540000000015
print(timeit.timeit('func_1(50)', number=100, globals=globals()))  # 0.023682369999999994
print(timeit.timeit('func_1(100)', number=100, globals=globals()))  # 0.075509728

cProfile.run('func_1(5000)')
# 1    1.708    1.708    1.720    1.720 task_4_1.py:10(func_1)
cProfile.run('func_1(7000)')
# 1    3.612    3.612    3.629    3.629 task_4_1.py:10(func_1)
cProfile.run('func_1(10000)')
# 1    7.221    7.221    7.267    7.267 task_1.py:11(func_1)


# 2 вариант
def func_2(n):
    a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    counter = {}
    frequency = 1
    num = None
    for item in a:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return f'Число {num} встречается {frequency} раз(а)'
    else:
        return f'Все элементы уникальны'


print(timeit.timeit('func_2(10)', number=100, globals=globals()))  # 0.001491753999999998
print(timeit.timeit('func_2(20)', number=100, globals=globals()))  # 0.002836938000000004
print(timeit.timeit('func_2(50)', number=100, globals=globals()))  # 0.007281777999999996
print(timeit.timeit('func_2(100)', number=100, globals=globals()))  # 0.023596247

cProfile.run('func_2(5000)')
# 5000    0.004    0.000    0.008    0.000 random.py:200(randrange)
cProfile.run('func_2(7000)')
# 7000    0.006    0.000    0.012    0.000 random.py:200(randrange)
cProfile.run('func_2(10000)')
# 10000    0.008    0.000    0.017    0.000 random.py:200(randrange)


# 3 вариант
def func_3(n):
    a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    a_set = set(a)
    num = None
    most_common = 1
    for number in a_set:
        frequency = a.count(number)
        if frequency > most_common:
            most_common = frequency
            num = number

    return f'Число {num} встречается {most_common} раз(а)' if most_common > 1 else 'Все элементы уникальны'


print(timeit.timeit('func_3(10)', number=100, globals=globals()))  # 0.0017880489999999999
print(timeit.timeit('func_3(20)', number=100, globals=globals()))  # 0.0035251350000000056
print(timeit.timeit('func_3(50)', number=100, globals=globals()))  # 0.010321776999999997
print(timeit.timeit('func_3(100)', number=100, globals=globals()))  # 0.024845432000000008

cProfile.run('func_3(5000)')
# 100    0.009    0.000    0.009    0.000 {method 'count' of 'list' objects}
cProfile.run('func_3(7000)')
# 100    0.013    0.000    0.013    0.000 {method 'count' of 'list' objects}
cProfile.run('func_3(10000)')
# 100    0.019    0.000    0.019    0.000 {method 'count' of 'list' objects}


# я проанализировала 3 варианта 4ой задачи из д/з 3 (один вариант взяла ваш).
# для каждой сделала по 4 замера timeit и по 3 замера cProfile
# вариант 1: затрачивет много времени из-за цикла в цикле
# вариант 2: самая эффективная и оптимальная
# вариант 3: слабое место - встроенная функция count
# N для timeit брала 10, 20, 50, 100;
# N для cProfile 5000, 7000, 10000
