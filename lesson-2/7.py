# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
from functools import reduce


def func1(n):
    return reduce(lambda x, y: x + y, range(n + 1))


def func2(n):
    return n * (n + 1) / 2


n = int(input('Введите число: '))
print(f'Равенство 1+2+...+n = n(n+1)/2 {["неверно", "верно"][func1(n) == func2(n)]}')
