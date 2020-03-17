import random
import timeit
import cProfile

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@memorize
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
while size <= 10000:
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(size, timeit.timeit("number_in_array(size)", number=100, globals=globals()))
    size *= 10




n = 1
while n <= 10000:
    print(n)
    cProfile.run("number_in_array(n)")
    n *= 10