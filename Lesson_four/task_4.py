# Поиск i-го простого числа, без использования алгоритма «Решето Эратосфена»

import timeit
import cProfile


def sieve_without_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


print(timeit.timeit('sieve_without_eratosthenes(10)', globals=globals(), number=100))  # 0.0012311999999999983
print(timeit.timeit('sieve_without_eratosthenes(100)', globals=globals(), number=100))  # 0.0540018
print(timeit.timeit('sieve_without_eratosthenes(1000)', globals=globals(), number=100))  # 4.1961438


cProfile.run("sieve_without_eratosthenes(10)")  # 1 |0.001 |0.001 |0.001 |0.001 task_4.py:6(sieve_without_eratosthenes)
cProfile.run("sieve_without_eratosthenes(100)")  # 1 |0.001 |0.001 |0.001 |0.001 task_4.py:6(sieve_without_eratosthenes)
cProfile.run("sieve_without_eratosthenes(1000)")  # 1 |0.043 |0.043 |0.048 |0.048 task_4.py:6(sieve_without_eratosthenes)

# Поиск i-го простого числа, без использования алгоритма «Решето Эратосфена» работает на мног быстре
# чем с использованием