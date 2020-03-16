# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_N = 2
END_N = 100
START_D = 2
END_D = 10

a = [0] * 8
for i in range(START_N, END_N):
    for j in range(START_D, END_D):
        if i % j == 0:
            a[j - 2] += 1

i = 0
while i < len(a):
    print(f"Число {i + 2} кратно - {a[i]}")
    i += 1