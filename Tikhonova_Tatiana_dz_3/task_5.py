# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

a = [2, -12, 7, 12, -8, 45, 2]

negative_numbers = []
max_num = 0
for number in a:
    if number < 0:
        negative_numbers.append(number)
print(negative_numbers)

for i in range(len(negative_numbers)):
    for k in range(i+1, len(negative_numbers)):
        if negative_numbers[i] > negative_numbers[k]:
            max_num = negative_numbers[i]
        else:
            max_num = negative_numbers[k]


if not negative_numbers:
    print('отрицательных чисел нет')
elif(len(negative_numbers)) == 1:
    print(f'максимальный отрицательный элемент {negative_numbers[0]}')
else:
    print(f'максимальный отрицательный элемент {max_num}')