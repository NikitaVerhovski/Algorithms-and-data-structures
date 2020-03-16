# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

mn = 0
mx = 0
for i in range(len(array)):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i

print(f"""
минимальное число - {array[mn]}
максимальное число - {array[mx]}
""")

array[mn], array[mx] = array[mx], array[mn]

print(f"{array}")