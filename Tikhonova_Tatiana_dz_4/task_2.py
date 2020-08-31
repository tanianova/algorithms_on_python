# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
# простое число делится само на себя и на 1
# index =        1  2  3  4  5  6
# prime_number = 2  3  5  7 11 13

n = 98


def prime(index):
    prime_numbers = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    while index < len(prime_numbers):
        return prime_numbers[index - 1]


def sieve(index):
    sieve_1 = [i for i in range(n)]
    sieve_1[1] = 0
    for i in range(2, n):
        if sieve_1[i] != 0:
            j = i + i
            while j < n:
                sieve_1[j] = 0
                j += i
    result = [i for i in sieve_1 if i != 0]
    while index < len(result):
        return result[index - 1]


print(sieve(5))
print(prime(5))
