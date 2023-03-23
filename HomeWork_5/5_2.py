# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum_n(a, b):
    if b < 0 < a:
        a, b = b, a
    if b == 0:
        return a
    return sum_n(a + 1, b - 1)

n = int(input())
m = int(input())
print(sum_n(n, m))