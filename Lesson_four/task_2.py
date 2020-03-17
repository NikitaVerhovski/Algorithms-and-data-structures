import random
import timeit
import cProfile


def number_in_array(array):

    num = array[0]
    max_frq = 1
    for i in range(size - 1):
        frq = 1
        for k in range(i + 1, size):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    if max_frq > 1:
        return f"{max_frq} раз(а) встечется число {num}"
    else:
        return f"Все элементы уникальны"


size = 1
while size <= 1000:
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(size, timeit.timeit("number_in_array(array)", number=100, globals=globals()))
    size *= 10
# 1 4.579999999999862e-05
# 10 0.0008049000000000008
# 100 0.0451138
# 1000 4.6826095

size = 1
while size <= 1000:
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(size)
    cProfile.run("number_in_array(array)")
    size *= 10

# 1
# 1    0.000    0.000    0.000    0.000 task_2.py:6(number_in_array)

# 10
# 1    0.000    0.000    0.000    0.000 task_2.py:6(number_in_array)

# 100
# 1    0.000    0.000    0.000    0.000 task_2.py:6(number_in_array)

# 1000
# 1    0.048    0.048    0.048    0.048 task_2.py:6(number_in_array)
