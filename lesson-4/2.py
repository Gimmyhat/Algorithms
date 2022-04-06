# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

from timeit import timeit


def get_n_primes_simple(n):
    i = 2
    while n > 1:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            n -= 1
    return i


def add_primes(min_num, max_num, prev_primes):
    ''' Добавляем простые числа и последние вычеркнутые числа '''
    nums = list(range(min_num, max_num + 1))
    for prime, last_removed in prev_primes.items():
        if last_removed < min_num:
            to_remove = range(last_removed + prime, max_num + 1, prime)
        else:
            to_remove = range(last_removed, max_num + 1, prime)
        for num in to_remove:
            nums[num - min_num] = 0
        prev_primes[prime] = to_remove[-1]
    # ищем новые простые
    for num in nums:
        # если равен нулю, то число вычеркнуто
        if num != 0:
            next_prime = num
            to_remove = range(next_prime * 2, max_num + 1, next_prime)
            for num1 in to_remove:
                nums[num1 - min_num] = 0
            if len(to_remove) > 0:
                prev_primes[next_prime] = to_remove[-1]
            else:
                prev_primes[next_prime] = 2 * next_prime


def get_n_primes(n):
    # Находит первые n или больше первых простых чисел
    min_num = 2
    max_num = 2 * n
    prev_primes = {}
    while len(prev_primes) < n:
        add_primes(min_num, max_num, prev_primes)
        min_num = max_num + 1
        max_num *= 2
    return list(prev_primes.keys())[n - 1]


# n = 500
# print(get_n_primes_simple(n))  # находит i-ое по счету простое число... например число под номером 500 - это 3571
# print(get_n_primes(n))  # делает то же самое, но быстрее

for i in range(100, 500, 100):
    n = i
    print(
        f"{n} "
        f"{timeit('get_n_primes_simple(n)', setup='from __main__ import get_n_primes_simple, n', number=100):.6f} "
        f"{timeit('get_n_primes(n)', setup='from __main__ import get_n_primes, n', number=100):.6f}")

# Первый способ имеет сложность O(n**2)
# Второй способ - для решета Эратосфена потребуется O(n*log(log(n))) операций. Потребление памяти составит O(n)

#  n    1           2
# 100 0.351924 0.037886
# 200 1.628214 0.125166
# 300 3.911707 0.220313
# 400 7.652096 0.265063

