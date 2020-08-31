# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def recursion(n):
    if n == 1:
        return n
    else:
        return n + recursion(n - 1)


def for_compare(n):
    return n * (n + 1) / 2


n = 1
while True:
    if recursion(n) == for_compare(n):
        print('равенство выполняется')
        n += 1
    else:
        print('равенство не выполняется')
        break

