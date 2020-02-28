# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#https://drive.google.com/file/d/19QNZ9vTmTy1ZFSJ_hA7NkJ28VULaS_pi/view?usp=sharing


def even_odd():
    x = int(input("Введите целое число :"))
    even = odd = 0
    while x > 0:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        x = x // 10
    return print(f"Четных чисел - {even} , нечетных чисел - {odd}")

even_odd()