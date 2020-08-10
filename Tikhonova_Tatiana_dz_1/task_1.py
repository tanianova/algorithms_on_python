# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

#https://drive.google.com/file/d/1QF_UCEJpIS34SClJ8Ym8f_6AZHD9ZXoD/view?usp=sharing

n = int(input('введите трехзначное число: '))
a = n // 100
b = n % 100 // 10
c = n % 10

print(f"сумма чисел равна {a+b+c}")
print(f"произведение чисел равно {a*b*c}")
