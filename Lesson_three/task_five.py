# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random


SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
index = -1
while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f"""
максимальный отрицательный элемент  {array[index]}
значение и позиция (индекс) в массиве  {index + 1}  
""")