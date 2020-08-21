# 6.В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

num = random.randint(1, 100)
print(num)

print('угадайте число за 10 попыток')
i = 0

while i < 10:
    user_num = int(input('введите число от 1 до 100: '))
    if user_num == num:
        print('вы угадали!')
        break
    elif user_num < num:
        print('ваше число меньше загаданного')
    else:
        print('ваше число больше загаданного')
    i += 1
else:
    print(f'число не угадано. правильное число - {num}')
