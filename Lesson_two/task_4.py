# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число

# https://drive.google.com/file/d/19QNZ9vTmTy1ZFSJ_hA7NkJ28VULaS_pi/view?usp=sharing

from random import random
x = round(random() * 100)
i = 1
while i <= 10:
    print("Для вас загадано рандомное число.\nУ вас есть 10 попыток")
    z = int(input(str(i) + "-я попытка : "))
    if z > x:
        print("Много")
    elif z < x:
        print("Мало")
    else:
        print(f"Вы угадали с {i}-й попытки")
        break
    i += 1
else:
    print("Вы исчерпали 10 попыток. Было загадано число - ", x)