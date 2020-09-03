# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. В сумму не включаем пустую строку и строку целиком.
import hashlib


def my_func(stroka):
    array = set()
    for i in range(len(stroka)):
        for j in range(1, len(stroka)):
            array.add(hashlib.sha1(stroka[i: i + j].encode('utf-8')).hexdigest())
    array -= {'', stroka}
    return len(array)


print(my_func('sova'))
