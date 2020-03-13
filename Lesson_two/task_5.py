# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/19QNZ9vTmTy1ZFSJ_hA7NkJ28VULaS_pi/view?usp=sharing

n = int(input("Введите целое число : "))
y = 1
z = 0
for i in range(n):
    z += y
    y /= -2
print(z)