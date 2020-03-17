# Поиска i-го простого числа, используя алгоритм «Решето Эратосфена»

import math
import timeit
import cProfile



def sieve_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    '''Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    '''

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number



print(timeit.timeit('sieve_eratosthenes(10)', globals=globals(), number=100))  # 0.005535100000000348
print(timeit.timeit('sieve_eratosthenes(100)', globals=globals(), number=100))  # 0.9581
print(timeit.timeit('sieve_eratosthenes(1000)', globals=globals(), number=100))  # 298.9867815

cProfile.run("sieve_eratosthenes(10)")  # 1 |0.000 |0.000 |0.000 |0.000 task_5.py:25(prime_counting_function)
cProfile.run("sieve_eratosthenes(100)")  # 1 |0.000 |0.000 |0.000 |0.000 task_5.py:25(prime_counting_function)
cProfile.run("sieve_eratosthenes(1000)")  # 1 |0.003 |0.003 |0.004 |0.004 task_5.py:25(prime_counting_function)

# Поиска i-го простого числа, используя алгоритм «Решето Эратосфена» работает на мног медленнее
