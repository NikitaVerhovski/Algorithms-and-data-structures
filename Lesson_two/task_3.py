# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# https://drive.google.com/file/d/19QNZ9vTmTy1ZFSJ_hA7NkJ28VULaS_pi/view?usp=sharing


def flip_numbers():
    x = int(input("Введите целое число :"))
    z = 0
    while x > 0:
        z = z * 10 + x % 10
        x = x // 10
    return print(z)

flip_numbers()




