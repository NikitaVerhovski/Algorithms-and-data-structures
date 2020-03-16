# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile


def number_in_array(size):

    array = [random.randint(size * -10, size * 10) for _ in range(size)]

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
    print(size, timeit.timeit("number_in_array(size)", number=100, globals=globals()))
    size *= 10


# 1 0.00023470000000000088
# 10 0.0022133000000000014
# 100 0.05929860000000001
# 1000 5.1792522000000005

n = 1
while n <= 10000:
    print(n)
    cProfile.run("number_in_array(n)")
    n *= 10

# cProfile.run("number_in_array(1)")  # 1    0.000    0.000    0.000    0.000 task_1.py:8(number_in_array)
# cProfile.run("number_in_array(10)")  # 1    0.001    0.001    0.001    0.001 task_1.py:8(number_in_array)
# cProfile.run("number_in_array(100)")  # 1    0.002    0.002    0.002    0.002 task_1.py:8(number_in_array)
# cProfile.run("number_in_array(1000)")  # 1    0.008    0.008    0.009    0.009 task_1.py:8(number_in_array)

