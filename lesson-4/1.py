# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import functools
import time
from math import prod


def timer(func):
    """Длительность работы функции"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        end = time.perf_counter()
        work_time = end - start
        print(f"Время выполнения {func.__name__!r}: {work_time:.4f} сек.")
        return val
    return wrapper


# Найти сумму и произведение цифр числа.
@timer
def get_sum_and_mult_1(n):
    nums = list(map(int, str(n)))
    print(f'Сумма цифр числа = {sum(nums)}\nпроизведение цифр числа = {prod(nums)}')

@timer
def get_sum_and_mult_2(n):
    s = 0
    m = 1
    while n:
        s += n % 10
        m *= n % 10
        n //= 10
    print(f'Сумма цифр числа = {s}\nпроизведение цифр числа = {m}')


if __name__ == '__main__':
    n = 12345789**10000
    get_sum_and_mult_1(n)  # сложность O(n)
    get_sum_and_mult_2(n)  # сложность O(n)

# Результат работы:

# Сумма цифр числа = 319311
# произведение цифр числа = 0
# Время выполнения 'get_sum_and_mult_1': 0.1991 сек.
# Сумма цифр числа = 319311
# произведение цифр числа = 0
# Время выполнения 'get_sum_and_mult_2': 5.1276 сек.


